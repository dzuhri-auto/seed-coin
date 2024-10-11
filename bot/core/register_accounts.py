import os

from pyrogram import Client

from bot.config import settings
from bot.utils import logger
from helpers import get_tele_user_obj_from_query_id

file_name = "query_ids.txt"


async def add_session() -> None:
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    logger.warning(
        "⚠️ Please only register account with userid below 61xxxx (check @userinfobot) otherwise your account will got banned !"
    )
    session_name = input("\nEnter the session name (press Enter to exit): ")

    if not session_name:
        return None

    session = Client(name=session_name, api_id=API_ID, api_hash=API_HASH, workdir="sessions/")

    async with session:
        user_data = await session.get_me()

    logger.success(
        f"Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}"
    )


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
