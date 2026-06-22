from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

from HMDMUSIC.utils.pluginloader import load_plugins
from HMDMUSIC.core.mongodb import ping_db

from flask import Flask
import asyncio
import threading
import os

web = Flask(__name__)

@web.route("/")
def home():
    return "HMDMUSIC is running ✅"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


app = Client(
    "HMDMUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

load_plugins()

asyncio.run(ping_db())

print("MongoDB Connected ✅")

threading.Thread(target=run_web, daemon=True).start()

print("Web Server Started ✅")

app.run()
