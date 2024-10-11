import os

from bot.utils import logger
from helpers import get_query_ids, get_session_names, get_tele_user_obj_from_query_id


async def delete_session():
    # global tg_clients

    session_names = get_session_names()
    number_validation = []
    if session_names:
        print("")
        print("Please Choose session that want to be delete. (press enter to exit): ")
        print("")
        for idx, session_name in enumerate(session_names):
            num = idx + 1
            print(f"{num}. {session_name}")
            number_validation.append(str(num))

        print("")
        while True:
            delete_action = input("> ")
            if not delete_action:
                return None

            if not delete_action.isdigit():
                logger.warning("Please only input number")
            elif delete_action not in number_validation:
                logger.warning("Please only input number that are available")
            else:
                delete_action = int(delete_action)
                break

        session_name_choosen = session_names[delete_action - 1]

        session_file = f"sessions/{session_name_choosen}.session"

        if os.path.exists(session_file):
            os.remove(session_file)
            logger.success(f"Session {session_name_choosen} successfully deleted")
    else:
        logger.warning(f"You dont have any session, please create session first!")


async def delete_query_id():
    delete = True
    while delete:
        query_ids = await get_query_ids()
        number_validation = []
        list_of_username = []
        delete_action = None

        if query_ids:
            print("")
            print("Please select the session you want to delete. (press enter to exit): ")
            print("")
            for idx, query_id in enumerate(query_ids):
                tele_user_obj = get_tele_user_obj_from_query_id(query_id)
                username = tele_user_obj.get("username")
                num = idx + 1
                print(f"{num}. {username}")
                list_of_username.append(username)
                number_validation.append(str(num))
            print("")

            while True:
                delete_action = input("> ")
                if not delete_action:
                    return None

                if not delete_action.isdigit():
                    logger.warning("Please only input number")
                elif delete_action not in number_validation:
                    logger.warning("Please only input number that are available")
                else:
                    delete_action = int(delete_action)
                    break

            with open("query_ids.txt", "r+") as f:
                content = f.readlines()
                content_len = len(content)
                f.truncate(0)
                f.seek(0)
                index_to_strip = 0
                for content_idx, line in enumerate(content):
                    if not content_idx == (delete_action - 1):
                        if delete_action == content_len:
                            index_to_strip = delete_action - 2
                        if index_to_strip and content_idx == index_to_strip:
                            f.write(line.strip())
                        else:
                            f.write(line)

            logger.success(f"Successfully delete session: {list_of_username[delete_action - 1]}")

            list_of_username.pop(delete_action - 1)

            if not list_of_username:
                logger.success(f"No session left")
                return None

            print("\n")
            keep_deleting = input("Do you want to delete another? (y/n) > ")
            if not keep_deleting or keep_deleting == "n":
                return None
            elif keep_deleting == "y":
                continue
            else:
                return None
        else:
            logger.warning(
                "No query ID found. Please select <lc>Add query</lc> or add it directly to the <lc>query_ids.txt</lc> file"
            )
            return None
