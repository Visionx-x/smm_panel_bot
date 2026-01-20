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
from handlers import all_handlers
import db  # keep if DB init happens here

# ==============================
# LOGGING
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ==============================
# HEALTH CHECK SERVER (IMPORTANT)
# ==============================
PORT = int(os.environ.get("PORT", 10000))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SMM Panel Bot is running")

def start_web_server():
    try:
        server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
        logger.info(f"🌐 Health server running on port {PORT}")
        server.serve_forever()
    except Exception as e:
        logger.error(f"Health server error: {e}")

# Start health server in background
threading.Thread(target=start_web_server, daemon=True).start()

# ==============================
# TELEGRAM BOT
# ==============================
app = Client(
    name="panel_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,        # better performance
    in_memory=True     # good for free hosting
)

# Register handlers
all_handlers(app)

logger.info("🚀 Starting SMM Panel Bot...")

# Run bot (blocking)
app.run()

logger.info("✅ Bot stopped")
