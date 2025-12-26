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
app = Client(
    "panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    in_memory=False  # Keeps session safe on Render restarts
)

# ---------------- LOAD HANDLERS ---------------- #
all_handlers(app)

print("🚀 Bot is starting on Render...")

# ---------------- FLASK KEEP-ALIVE ---------------- #
PORT = int(os.environ.get("PORT", 8080))  # Render assigns PORT automatically
server = Flask(__name__)

@server.route("/")
def home():
    return "Bot is running!"

def run_flask():
    server.run(host="0.0.0.0", port=PORT)

# Start Flask server in a separate thread
Thread(target=run_flask).start()

# ---------------- RUN BOT ---------------- #
app.run()
