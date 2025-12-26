# ============================================================
# Smm Panel Bot
# Author: learningbots79 (https://github.com/learningbots79) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

import logging
import os
from threading import Thread
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import all_handlers

# ---------------- LOGGING ---------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- PYROGRAM CLIENT ---------------- #
bot = Client(
    "panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    in_memory=False
)

# ---------------- LOAD HANDLERS ---------------- #
all_handlers(bot)

print("🚀 Starting SMM Panel Bot on Render...")

# ---------------- BOT THREAD ---------------- #
def run_bot():
    print("🤖 Pyrogram bot thread started...")
    bot.run()

# Start bot in background thread
Thread(target=run_bot, daemon=True).start()


# ---------------- FLASK KEEP-ALIVE (MAIN PROCESS) ---------------- #
app = Flask(__name__)

@app.route("/")
def home():
    return "SMM Panel Bot is alive!"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"🌐 Flask server running on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
