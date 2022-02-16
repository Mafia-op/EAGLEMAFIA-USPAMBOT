import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
        API_ID = os.environ.get("API_ID", None)
        API_HASH = os.environ.get("API_HASH", None)
        STRING_1 = os.environ.get("STRING_1", None)
        STRING_2 = os.environ.get("STRING_2", None)
        STRING_3 = os.environ.get("STRING_3", None)
        STRING_4 = os.environ.get("STRING_4", None)
        STRING_5 = os.environ.get("STRING_5", None)
        STRING_6 = os.environ.get("STRING_6", None)
        STRING_7 = os.environ.get("STRING_7", None)
        STRING_8 = os.environ.get("STRING_8", None)
        STRING_9 = os.environ.get("STRING_9", None)
        STRING_10 = os.environ.get("STRING_10", None) 
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        
else:
    class Config(object):
        DB_URI = None
