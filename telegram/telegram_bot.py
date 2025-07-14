# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Custom design products
CUSTOM_DESIGNS = {
    "Buy Custom eBook Cover Design – $499": "https://inkstory-api.onrender.com/buy/ebook-only",
    "Buy Custom Print & eBook Cover Design – $699": "https://inkstory-api.onrender.com/buy/print-and-ebook",
}

# Premade design products
PREMADE_DESIGNS = {
    "3022 Premade Book Cover Design – $5,000": "https://inkstory-api.onrender.com/buy/3022",
    "Dark Wizard Premade Book Cover Design – $3,900": "https://inkstory-api.onrender.com/buy/dark-wizard",
    "Eternal Runes Premade Book Cover Design – $2,700": "https://inkstory-api.onrender.com/buy/eternal-runes",
    "Oracle Premade Book Cover Design – $1,000": "https://inkstory-api.onrender.com/buy/oracle",
    "Premade Book Cover Design #8 – $900": "https://inkstory-api.onrender.com/buy/premade-8",
    "Premade Book Cover Design #7 – $1,100": "https://inkstory-api.onrender.com/buy/premade-7",
    "Premade Book Cover Design #6 – $800": "https://inkstory-api.onrender.com/buy/premade-6",
    "Premade Book Cover Design #5 – $990": "https://inkstory-api.onrender.com/buy/premade-5",
    "Premade Book Cover Design #4 – $900": "https://inkstory-api.onrender.com/buy/premade-4",
    "Premade Book Cover Design #3 – $1,200": "https://inkstory-api.onrender.com/buy/premade-3",
    "Premade Book Cover Design #2 – $900": "https://inkstory-api.onrender.com/buy/premade-2",
    "Premade Book Cover Design #1 – $600": "https://inkstory-api.onrender.com/buy/premade-1",
}

def start(update, context):
    message = (
        "Welcome to InkStory Bot! 🤖📚\n\n"
        "For writers & authors on Telegram, you can buy book cover designs instantly here.\n"
        "Type /help to see what I can do.\n\n"
        "Or shop directly at: https://inkstorydesigns.com"
    )
    update.message.reply_text(message)

def help_command(update, context):
    message = (
        "*Available Commands:*\n"
        "/start - Show welcome message\n"
        "/help - Show this help info\n"
        "/buy - View all book cover design packages\n\n"
        "*How to Buy:*\n"
        "1. Type /buy and tap a product\n"
        "2. Pay securely via Stripe\n"
        "3. Fill out the design order form after redirect\n\n"
        "_Your book cover design will be emailed after completion (usually within around 3-5 days)._\n\n"
        "Visit https://inkstorydesigns.com or email inkstorydesign@gmail.com for help."
    )
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def buy(update, context):
    message = "*🛒 Buy Custom Book Cover Design Packages:*\n"
    for name, url in CUSTOM_DESIGNS.items():
        message += f"• [{name}]({url})\n"

    message += "\n*🧙 Buy Premade Book Cover Designs:*\n"
    for name, url in PREMADE_DESIGNS.items():
        message += f"• [{name}]({url})\n"

    message += (
        "\n*How to Buy:*\n"
        "1. Tap a link above\n"
        "2. Pay securely with Stripe\n"
        "3. Complete the form after redirect\n\n"
        "_Your book cover will be emailed after completion._"
    )

    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN is not set.")
        return

    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("buy", buy))

    updater.start_polling()
    print("✅ InkStory Bot is running on Telegram...")
    updater.idle()

if __name__ == "__main__":
    main()
