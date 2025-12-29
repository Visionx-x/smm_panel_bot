# ============================================================
# Smm Panel Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

import os
from pyrogram import Client
from flask import Flask
import threading

# Import handlers from handlers/__init__.py
from handlers import all_handlers


# ==============================
# Flask – Health Check (Render)
# ==============================
web = Flask(__name__)

@web.get("/health")
def health():
    return "OK", 200


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)


# ==============================
# Pyrogram App
# ==============================
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "smm_panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,  # fast handlers
)


# ==============================
# Start Bot + Load Handlers
# ==============================
@app.on_raw_update()
async def _(*args, **kwargs):
    # Dummy listener so Pyrogram fully starts
    pass


def start_bot():
    print("🔄 Starting SMM Panel Bot...")

    # REGISTER ALL HANDLERS
    all_handlers(app)

    # Start Flask in a thread (Render requirement)
    threading.Thread(target=run_web).start()

    # Start Pyrogram
    app.run()

    print("🚀 Bot is running!")


if __name__ == "__main__":
    start_bot()
