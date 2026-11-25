import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "9296306156:AAE0_RHdxFf6sIU-2wF9UbOqJoMq0gOrfiQ"
ADMIN_ID = 7382151908  # Replace with the designated numeric Telegram ID
PHOTO_PATH = "botpics.jpg"  # Or a direct https:// image URL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    # 1. Notify the designated admin account
    username = f"@{user.username}" if user.username else "No username"
    admin_text = (
        f"🆕 New Bot User!\n\n"
        f"Name: {user.full_name}\n"
        f"Username: {username}\n"
        f"User ID: `{user.id}`"
    )
    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=admin_text,
            parse_mode="Markdown",
        )
    except Exception as e:
        logging.error(f"Failed to send admin notification: {e}")

    # 2. Send the welcome photo & buttons to the user
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
