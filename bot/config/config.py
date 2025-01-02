import json
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    REF_ID = os.getenv("REF_ID", "")

    AUTO_BUY_WORM = os.getenv("AUTO_BUY_WORM", "False")
    AUTO_UPGRADE = os.getenv("AUTO_UPGRADE", "True")
    MIN_CLAIM_GUILD_AMOUNT = int(os.getenv("MIN_CLAIM_GUILD_AMOUNT", "7"))
    AUTO_SPIN = os.getenv("AUTO_SPIN", "True")
    AUTO_FUSION = os.getenv("AUTO_FUSION", "False")
    AUTO_HATCH = os.getenv("AUTO_HATCH", "False")
    AUTO_SELL_WORM = os.getenv("AUTO_SELL_WORM", "False")
    
    USE_RANDOM_DELAY_IN_RUN = os.getenv("AUTO_UPGRADE", "True")
    RANDOM_DELAY_IN_RUN = json.loads(os.getenv("RANDOM_DELAY_IN_RUN", "[5, 15]"))
    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", "False")


settings = Settings()
