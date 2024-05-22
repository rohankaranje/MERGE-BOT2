import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", '411ca710711b1f6658dcb4723a51a886')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7122272836:AAE_zYHR0ZG24oo8TQ1vmeWGwsnnq2eNTXc")
    TELEGRAM_API = os.environ.get("TELEGRAM_API",'15630493')
    OWNER = os.environ.get("OWNER", "1315497648")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "vedu")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://test:test@cluster0.47luuoj.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", '-1002138249832')  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
