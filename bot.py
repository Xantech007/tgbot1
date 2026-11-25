from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "9296306156:AAE0_RHdxFf6sIU-2wF9UbOqJoMq0gOrfiQ"
PHOTO_PATH = "banner.jpg"  # Replace with your local image path or a direct https:// image URL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                "JOIN CHANNEL NOW", url="https://t.me/pay1cashapp"
            )
        ],
        [
            InlineKeyboardButton(
                "WATCH THE FULL VIDEO TUTORIAL",
                url="https://t.me/pay1cashapp/579",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = """👋 Welcome to the CashApp Tutorial Bot!

I’m here to guide you step-by-step so you can start earning on CashApp the right way.

✅ What you’ll get:
• A valid referral link
• How to register correctly
• Full video tutorial on how CashApp works

Join our official Telegram channel to get the complete tutorial and updates:

➡️ https://t.me/pay1cashapp

Let’s start making that monthly cash! 💰"""

    # If PHOTO_PATH is a URL, pass photo=PHOTO_PATH directly instead of open(...)
    with open(PHOTO_PATH, "rb") as photo_file:
        await update.message.reply_photo(
            photo=photo_file,
            caption=caption,
            reply_markup=reply_markup,
        )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
