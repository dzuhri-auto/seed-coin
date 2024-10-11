import glob
import json
import os
from datetime import datetime, timedelta, timezone
from urllib.parse import unquote

from better_proxy import Proxy
from pyrogram import Client

from bot.config import settings
from bot.exceptions import MissingApiKeyException, MissingTelegramAPIException
from constants import WormRarityConstants


def calculate_real_number(number):
    return number / 1000000000


def update_or_add_dict(list_of_dicts, key, key_value, new_data):
    """
    Updates a dictionary in a list of dictionaries if the key exists, otherwise adds a new dictionary.

    :param list_of_dicts: List of dictionaries to update or add to.
    :param key: The key to check for existence in each dictionary.
    :param key_value: The value of the key to match.
    :param new_data: The data to update or add to the dictionary.
    """
    for dictionary in list_of_dicts:
        if dictionary.get(key) == key_value and dictionary.get("upgrade_lvl") < new_data.get(
            "upgrade_lvl"
        ):
            dictionary.update(new_data)
            return
    # If the key_value is not found, add a new dictionary
    # new_dict = {key: key_value}
    # new_dict.update(new_data)
    list_of_dicts.append(new_data)


def get_session_names() -> list[str]:
    session_names = glob.glob("sessions/*.session")
    session_names = [os.path.splitext(os.path.basename(file))[0] for file in session_names]

    return session_names


def check_license_key():
    if not settings.LICENSE_KEY:
        raise MissingApiKeyException("LICENSE KEY is missing, please check your .env file!")


def check_telegram_api():
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    if not API_ID or not API_HASH:
        raise MissingTelegramAPIException(
            "API_ID and API_HASH is missing, please check your .env file!"
        )


async def get_tg_clients() -> list[Client]:
    # global tg_clients

    tg_clients = []
    session_names = get_session_names()

    # if not session_names:
    #     raise FileNotFoundError("Not found session files")

    # if not settings.API_ID or not settings.API_HASH:
    #     raise ValueError("API_ID and API_HASH not found in the .env file.")
    if session_names:
        tg_clients = [
            Client(
                name=session_name,
                api_id=settings.API_ID,
                api_hash=settings.API_HASH,
                workdir="sessions/",
                plugins=dict(root="bot/plugins"),
            )
            for session_name in session_names
        ]

    return tg_clients


# def create_menus():
#     menus = [
#         "Start bot using session",
#         "Start bot using query",
#         "Add session",
#         "Add query",
#         "Delete session",
#         "Delete query",
#     ]
#     print("Please choose menu: ")
#     print("")
#     total_menu = 0
#     for idx, menu in enumerate(menus):
#         num = idx + 1
#         total_menu += 1
#         print(f"{num}. {menu}")
#     print(
#         "========================================================================================"
#     )
#     return total_menu


def create_menus():
    menus = [
        "Start bot",
        "Add session",
        "Delete session",
    ]
    print("Please choose menu: ")
    print("")
    total_menu = 0
    for idx, menu in enumerate(menus):
        num = idx + 1
        total_menu += 1
        print(f"{num}. {menu}")
    print(
        "========================================================================================"
    )
    return total_menu


def get_proxies() -> list[Proxy]:
    if settings.USE_PROXY_FROM_FILE.lower() == "true":
        with open(file="bot/config/proxies.txt", encoding="utf-8-sig") as file:
            proxies = [Proxy.from_str(proxy=row.strip()).as_url for row in file]
    else:
        proxies = []
    return proxies


def convert_datetime_str_to_utc(datetime_str):
    decimal_index = datetime_str.find(".")
    if decimal_index != -1:
        # Ensure only 3 digits after the decimal point for milliseconds
        datetime_str = datetime_str[: decimal_index + 4]

    return datetime.fromisoformat(datetime_str).replace(tzinfo=timezone.utc)


def format_duration(seconds):
    message = ""
    duration_td = timedelta(seconds=seconds)
    days, day_remainder = divmod(duration_td.total_seconds(), 86400)
    hours, remainder = divmod(day_remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days:
        message = f"{int(days)} days "

    if hours:
        message = message + f"{int(hours)} hours "

    if minutes:
        message = message + f"{int(minutes)} minute "

    if seconds:
        message = message + f"{int(seconds)} seconds"
    return message.strip()


def mapping_role_color(role):
    if role == "admin":
        role = f"<lg>{role}</lg>"
    elif role == "premium":
        role = f"<lc>{role}</lc>"

    return role


def decode_query_id(query_id):
    query_string = query_id
    if "tgWebAppData" in query_id:
        query_string = unquote(
            string=query_id.split("tgWebAppData=", maxsplit=1)[1].split(
                "&tgWebAppVersion", maxsplit=1
            )[0]
        )
    parameters = query_string.split("&")
    decoded_pairs = [(param.split("=")[0], unquote(param.split("=")[1])) for param in parameters]
    result = dict()
    for key, value in decoded_pairs:
        result[key] = value

    reassign(result)
    return result


def reassign(d):
    """
    check if you have a dict after using literal_eval and reassign
    """
    for k, v in d.items():
        if v[0] in {"{", "["}:
            try:
                evald = json.loads(v)
                if isinstance(evald, dict):
                    d[k] = evald
            except ValueError as err:
                pass


async def get_query_ids():
    temp_lines = []
    with open("query_ids.txt", "r") as file:
        temp_lines = file.readlines()

    lines = [line.strip() for line in temp_lines]
    return lines


def get_tele_user_obj_from_query_id(query_id):
    # formatted_query_id = unquote(string=query_id)
    query_obj = decode_query_id(query_id)
    tele_user_obj = query_obj.get("user", {})
    return tele_user_obj


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def format_hunt_reward(hunt_reward={}):
    message = ""
    egg_type = hunt_reward.get("egg_type")
    worm_type = hunt_reward.get("worm_type")
    seed_amount = hunt_reward.get("seed_amount")
    if egg_type:
        message = f"Egg: {egg_type}, "

    if worm_type:
        message = message + f"Worm: {colorize_worm_by_rarity(worm_type)}, "

    if seed_amount:
        message = message + f"Seed: <lg>{calculate_real_number(seed_amount)}</lg>"
    return message


def claim_hour_by_storage(storage_level):
    if storage_level == 0:
        return 2
    elif storage_level == 1:
        return 3
    elif storage_level == 2:
        return 4
    elif storage_level == 3:
        return 6
    elif storage_level == 4:
        return 12
    else:
        return 24


def colorize_worm_by_rarity(worm_type):
    msg = worm_type
    if worm_type == WormRarityConstants.LEGENDARY:
        msg = f"<lr>{worm_type}</lr>"

    if worm_type == WormRarityConstants.EPIC:
        msg = f"<lm>{worm_type}</lm>"

    if worm_type == WormRarityConstants.RARE:
        msg = f"<e>{worm_type}</e>"

    if worm_type == WormRarityConstants.UNCOMMON:
        msg = f"<lg>{worm_type}</lg>"

    return msg


def order_worms_by_rarity(worm_datas=[]):
    sorted_worms_datas = []
    legendary_worms = []
    epic_worms = []
    rare_worms = []
    uncommon_worms = []
    common_worms = []
    total_worms = {
        WormRarityConstants.LEGENDARY: 0,
        WormRarityConstants.EPIC: 0,
        WormRarityConstants.RARE: 0,
        WormRarityConstants.UNCOMMON: 0,
        WormRarityConstants.COMMON: 0,
    }
    for worm in worm_datas:
        worm_id = worm.get("id")
        worm_type = worm.get("type")
        temp_dict = {"worm_id": worm_id, "worm_type": worm_type}

        if worm_type == WormRarityConstants.LEGENDARY:
            legendary_worms.append(temp_dict)
            total_worms[WormRarityConstants.LEGENDARY] += 1
        elif worm_type == WormRarityConstants.EPIC:
            epic_worms.append(temp_dict)
            total_worms[WormRarityConstants.EPIC] += 1
        elif worm_type == WormRarityConstants.RARE:
            rare_worms.append(temp_dict)
            total_worms[WormRarityConstants.RARE] += 1
        elif worm_type == WormRarityConstants.UNCOMMON:
            uncommon_worms.append(temp_dict)
            total_worms[WormRarityConstants.UNCOMMON] += 1
        else:
            common_worms.append(temp_dict)
            total_worms[WormRarityConstants.COMMON] += 1

    sorted_worms_datas = legendary_worms + epic_worms + rare_worms + uncommon_worms + common_worms
    return sorted_worms_datas, total_worms


def populate_not_completed_tasks(task_datas=[]):
    not_completed_tasks = []
    for task in task_datas:
        if task.get("type") in ["sign-in"]:
            continue
        if not task.get("task_user") or not task.get("task_user", {}).get("completed"):
            not_completed_tasks.append(task)
    return not_completed_tasks
