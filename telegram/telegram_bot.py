# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    user_id = update.effective_user.id
    custom_designs = {
        "Buy Custom eBook Cover Design – $499": f"https://inkstory-api.onrender.com/buy/ebook-only?telegram_user_id={user_id}",
        "Buy Custom Print & eBook Cover Design – $699": f"https://inkstory-api.onrender.com/buy/print-and-ebook?telegram_user_id={user_id}",
    }

    premade_designs = {
        "3022 Premade Book Cover Design – $5,000": f"https://inkstory-api.onrender.com/buy/3022?telegram_user_id={user_id}",
        "Dark Wizard Premade Book Cover Design – $3,900": f"https://inkstory-api.onrender.com/buy/dark-wizard?telegram_user_id={user_id}",
        "Eternal Runes Premade Book Cover Design – $2,700": f"https://inkstory-api.onrender.com/buy/eternal-runes?telegram_user_id={user_id}",
        "Oracle Premade Book Cover Design – $1,000": f"https://inkstory-api.onrender.com/buy/oracle?telegram_user_id={user_id}",
        "Premade Book Cover Design #8 – $900": f"https://inkstory-api.onrender.com/buy/premade-8?telegram_user_id={user_id}",
        "Premade Book Cover Design #7 – $1,100": f"https://inkstory-api.onrender.com/buy/premade-7?telegram_user_id={user_id}",
        "Premade Book Cover Design #6 – $800": f"https://inkstory-api.onrender.com/buy/premade-6?telegram_user_id={user_id}",
        "Premade Book Cover Design #5 – $990": f"https://inkstory-api.onrender.com/buy/premade-5?telegram_user_id={user_id}",
        "Premade Book Cover Design #4 – $900": f"https://inkstory-api.onrender.com/buy/premade-4?telegram_user_id={user_id}",
        "Premade Book Cover Design #3 – $1,200": f"https://inkstory-api.onrender.com/buy/premade-3?telegram_user_id={user_id}",
        "Premade Book Cover Design #2 – $900": f"https://inkstory-api.onrender.com/buy/premade-2?telegram_user_id={user_id}",
        "Premade Book Cover Design #1 – $600": f"https://inkstory-api.onrender.com/buy/premade-1?telegram_user_id={user_id}",
    }

    message = (
        "Welcome to InkStory Bot! 🤖📚\n\n"
        "Order your custom or premade book cover instantly — right here in Telegram!\n\n"
        "Type /help to see what I can do.\n\n"
        "Choose a book cover design option below to begin\n\n"
        "*🛒 Custom Book Cover Design Options:*\n"
    )
    for name, url in custom_designs.items():
        message += f"• [{name}]({url})\n"

    message += "\n*🧙 Premade Book Cover Design Options:*\n"
    for name, url in premade_designs.items():
        message += f"• [{name}]({url})\n"

    message += (
        "\n*How it works:*\n"
        "1. Tap an option above\n"
        "2. Pay securely with Stripe\n"
        "3. Complete the form after redirect\n\n"
        "📬 Your cover will be delivered to your email (usually in 3–5 days).\n\n"
        "Need help? Visit https://inkstorydesigns.com or email inkstorydesign@gmail.com"
    )

    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

def help_command(update, context):
    message = (
        "*Available Commands:*\n"
        "/start - Show welcome message\n"
        "/help - Show this help info\n"
        "/buy - View all book cover design packages\n"
        "/contact - Get support from Ink Story Designs\n\n"
        "*How to Buy:*\n"
        "1. Type /buy and tap a product\n"
        "2. Pay securely via Stripe\n"
        "3. Fill out the design order form after redirect\n\n"
        "_Your book cover design will be emailed after completion (usually within around 3–5 days)._\n\n"
        "Visit https://inkstorydesigns.com or email inkstorydesign@gmail.com for help."
    )
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def buy(update, context):
    user_id = update.effective_user.id
    custom_designs = {
        "Buy Custom eBook Cover Design – $499": f"https://inkstory-api.onrender.com/buy/ebook-only?telegram_user_id={user_id}",
        "Buy Custom Print & eBook Cover Design – $699": f"https://inkstory-api.onrender.com/buy/print-and-ebook?telegram_user_id={user_id}",
    }

    premade_designs = {
        "3022 Premade Book Cover Design – $5,000": f"https://inkstory-api.onrender.com/buy/3022?telegram_user_id={user_id}",
        "Dark Wizard Premade Book Cover Design – $3,900": f"https://inkstory-api.onrender.com/buy/dark-wizard?telegram_user_id={user_id}",
        "Eternal Runes Premade Book Cover Design – $2,700": f"https://inkstory-api.onrender.com/buy/eternal-runes?telegram_user_id={user_id}",
        "Oracle Premade Book Cover Design – $1,000": f"https://inkstory-api.onrender.com/buy/oracle?telegram_user_id={user_id}",
        "Premade Book Cover Design #8 – $900": f"https://inkstory-api.onrender.com/buy/premade-8?telegram_user_id={user_id}",
        "Premade Book Cover Design #7 – $1,100": f"https://inkstory-api.onrender.com/buy/premade-7?telegram_user_id={user_id}",
        "Premade Book Cover Design #6 – $800": f"https://inkstory-api.onrender.com/buy/premade-6?telegram_user_id={user_id}",
        "Premade Book Cover Design #5 – $990": f"https://inkstory-api.onrender.com/buy/premade-5?telegram_user_id={user_id}",
        "Premade Book Cover Design #4 – $900": f"https://inkstory-api.onrender.com/buy/premade-4?telegram_user_id={user_id}",
        "Premade Book Cover Design #3 – $1,200": f"https://inkstory-api.onrender.com/buy/premade-3?telegram_user_id={user_id}",
        "Premade Book Cover Design #2 – $900": f"https://inkstory-api.onrender.com/buy/premade-2?telegram_user_id={user_id}",
        "Premade Book Cover Design #1 – $600": f"https://inkstory-api.onrender.com/buy/premade-1?telegram_user_id={user_id}",
    }

    message = "*🛒 Buy Custom Book Cover Design Packages:*\n"
    for name, url in custom_designs.items():
        message += f"• [{name}]({url})\n"

    message += "\n*🧙 Buy Premade Book Cover Designs:*\n"
    for name, url in premade_designs.items():
        message += f"• [{name}]({url})\n"

    message += (
        "\n*How to Buy:*\n"
        "1. Tap a link above\n"
        "2. Pay securely with Stripe\n"
        "3. Complete the form after redirect\n\n"
        "_Your book cover will be emailed after completion._"
    )

    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

def contact(update, context):
    message = (
        "*Available Commands:*\n"
        "/start - Show welcome message\n"
        "/help - Show this help info\n"
        "/buy - View all book cover design packages\n"
        "/contact - Get support from Ink Story Designs\n\n"
        "*How to Buy:*\n"
        "1. Type /buy and tap a product\n"
        "2. Pay securely via Stripe\n"
        "3. Fill out the design order form after redirect\n\n"
        "_Your book cover design will be emailed after completion (usually within around 3–5 days)._\n\n"
        "Visit https://inkstorydesigns.com/#contact or email inkstorydesign@gmail.com for help."
    )
    update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def main():
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN is not set.")
        return

    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(CommandHandler("contact", contact))

    updater.start_polling()
    print("InkStory Bot is running on Telegram...")
    updater.idle()

if __name__ == "__main__":
    main()
