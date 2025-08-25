#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

async def start(update, context):
    await update.message.reply_text("✅ Bot çalışıyor! İngilizce pratik hazır.")

def run_http():
    port = int(os.environ.get("PORT", 10000))   # Render’ın verdiği PORT’u al
    print(f"Starting health server on port {port}")
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

def run_bot():
    if not TOKEN:
        raise ValueError("TELEGRAM_TOKEN yok!")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started. Polling ...")
    app.run_polling()

if __name__ == "__main__":
    # HTTP server thread
    threading.Thread(target=run_http, daemon=True).start()
    # Telegram bot polling
    run_bot()ü
