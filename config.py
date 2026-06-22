from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL")

STRING_SESSION = getenv("STRING_SESSION")

OWNER_ID = int(getenv("OWNER_ID"))

OWNER_NAME = getenv("OWNER_NAME")

OWNER_USERNAME = getenv("OWNER_USERNAME")

OWNER_BIO = getenv("OWNER_BIO")

OWNER_PHOTO = getenv("OWNER_PHOTO")
