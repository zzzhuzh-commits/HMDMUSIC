from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

from HMDMUSIC.utils.pluginloader import load_plugins

from flask import Flask
import threading
import os

web = Flask(__name__)

@web.route("/")
def home():
    return "HMDMUSIC is running ✅"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False
    )

app = Client(
    "HMDMUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

threading.Thread(
    target=run_web,
    daemon=True
).start()

print("Web Server Started ✅")

load_plugins()
print("Plugins Loaded ✅")

print("Starting Telegram Bot...")
app.start()
print("Bot Started Successfully ✅")

idle()

app.stop()
