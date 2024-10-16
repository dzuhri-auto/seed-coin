from .logger import logger, info, warning, debug, success, error, critical

import os

if not os.path.exists(path="sessions"):
    os.mkdir(path="sessions")

if not os.path.exists(path="bad_sessions"):
    os.mkdir(path="bad_sessions")

# if not os.path.exists("query_ids.txt"):
#     with open("query_ids.txt", "w"):
#         pass
