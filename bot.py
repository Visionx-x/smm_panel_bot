# ============================================================
# SMM Panel Bot
# Author: learningbots79 (https://github.com/learningbots79)
# Support: https://t.me/LearningBotsCommunity
# ============================================================

import os
import logging
import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import all_handlers

# ------------- LOGGING ------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ------------- PYROGRAM CLIENT ------------- #
bot = Client(
    "panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50
)

# Load handlers
all_handlers(bot)
print("✅ Handlers loaded")


# ------------- BOT RUNNER (THREAD SAFE) ------------- #
def run_bot():
    print("🤖 Starting Pyrogram bot thread...")

    # Create event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        bot.run()
    except Exception as e:
        print("❌ Bot crashed:", e)


# Start bot in background thread
Thread(target=run_bot, daemon=True).start()


# ------------- FLASK KEEP-ALIVE ------------- #
app = Flask(__name__)

@app.route("/")
def home():
    return "SMM Panel Bot is alive!"

@app.route("/health")
def health():
    return "OK"


# ------------- START FLASK (MAIN PROCESS) ------------- #
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"🌐 Flask server running on port {port}")
    app.run(host="0.0.0.0", port=port)
