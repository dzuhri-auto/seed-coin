import os
from itertools import cycle

from better_proxy import Proxy
from telethon import TelegramClient

from bot.config import settings
from bot.utils import logger, success
from helpers import get_proxies, get_tele_user_obj_from_query_id

file_name = "query_ids.txt"


async def add_session() -> None:
    proxies = get_proxies()
    proxies_cycle = cycle(proxies) if proxies else None
    create_session = True
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH
    # API_ID = 10840
    # API_HASH = "33c45224029d59cb3ad0c16134215aeb"
    session_folder = "sessions"
    if not os.path.exists(session_folder):
        os.makedirs(session_folder)
    logger.warning(
        "⚠️ Please register an account with a user ID below 63xxxx (check @userinfobot); otherwise, your account may be at risk of being banned!"
    )
    while create_session:
        session_name = input("\nPlease enter the session name (press Enter to exit): ")
        if not session_name:
            break
        session_path = os.path.join(session_folder, session_name)
        proxy_str = next(proxies_cycle) if proxies_cycle else None
        if proxy_str:
            proxy = Proxy.from_str(proxy_str)
            print(f"using proxy : {proxy}")
            proxy_dict = dict(
                proxy_type=proxy.protocol,
                addr=proxy.host,
                port=proxy.port,
                username=proxy.login,
                password=proxy.password,
            )
            client = TelegramClient(
                session_path,
                API_ID,
                API_HASH,
                proxy=proxy_dict,
            )
        else:
            client = TelegramClient(
                session_path,
                API_ID,
                API_HASH,
            )

        async with client:
            await client.start()
            print("\n")
            success(
                f"Session named <lg>{session_name}</lg> created. New Telethon session successfully saved in <lc>{session_path}.session</lc>."
            )

        create_more_session = input(
            "\nDo you want to add more sessions? [y/n] (press Enter to exit): "
        )
        if not create_more_session:
            break

        if create_more_session != "y":
            break


async def add_query_id():
    add = True
    while add:
        query_id = input("\nPlease input query id (press Enter to exit): ")

        if not query_id:
            break

        tele_user_obj = get_tele_user_obj_from_query_id(query_id)
        username = tele_user_obj.get("username")
        first_name = tele_user_obj.get("first_name")
        last_name = tele_user_obj.get("last_name")

        if os.path.exists(file_name):
            # Open the file in append mode and add the input value
            with open(file_name, "a") as file:
                file.write(query_id + "\n")
                logger.success(
                    f"Successfully added @{username} | {first_name} {last_name} to {file_name}"
                )
        else:
            logger.success(f"{file_name} does not exist.")
