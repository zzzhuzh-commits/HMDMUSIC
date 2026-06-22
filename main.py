from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

from HMDMUSIC.utils.pluginloader import load_plugins
from HMDMUSIC.core.mongodb import ping_db

import asyncio

app = Client(
    "HMDMUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

try:
    load_plugins()
    print("Plugins Loaded ✅")
except Exception as e:
    print(f"Plugin Error: {e}")
    raise

try:
    asyncio.run(ping_db())
    print("MongoDB Connected ✅")
except Exception as e:
    print(f"MongoDB Error: {e}")
    raise

print("Bot Starting ✅")

app.run()
