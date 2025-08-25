#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

# Ortam değişkenlerini yükle (.env veya Render env vars)
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("✅ Bot çalışıyor! İngilizce pratik yapmaya hazır.")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_TOKEN bulunamadı!")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started. Polling ...")
    app.run_polling()

if __name__ == "__main__":
    main()
