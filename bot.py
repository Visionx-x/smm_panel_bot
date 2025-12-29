# ============================================================
# SMM Panel Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial)
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

import os
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import all_handlers  # your register_start_handler inside handlers/__init__.py
from db import db

# ==============================
# LOGGING
# ==============================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ==============================
# WEB SERVER (Render / Health check)
# ==============================
PORT = int(os.environ.get("PORT", 10000))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SMM Panel Bot is running")

def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logger.info(f"Web server running on port {PORT}")
    server.serve_forever()

threading.Thread(target=start_web_server, daemon=True).start()

# ==============================
# TELEGRAM BOT
# ==============================
app = Client(
    "smm_panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,  # fast handlers
    in_memory=True
)

# REGISTER ALL HANDLERS
all_handlers(app)

logger.info("🔄 Starting SMM Panel Bot...")

# START BOT
app.run()

logger.info("🚀 Bot is running!")
