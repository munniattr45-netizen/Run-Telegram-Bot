import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ==== আপনার কনফিগারেশন ====
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Secrets থেকে পড়বে
OWNER_USERNAME = "RASEL_B_D_T_148589"
ADMIN_USERNAME = "RASEL_B_D_T_148589"
MINI_APP_URL = "t.me/Ai_hackbdtbot/curiousbombolonee31880"
# ===========================

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "..."  # তোমার আগের text এখানে রাখো

    keyboard = [
        [InlineKeyboardButton("🎁 Owner Contact", url=f"https://t.me/{OWNER_USERNAME}")],
        [InlineKeyboardButton("🤖 Ai Hack Bot ", url=MINI_APP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)

# /help কমান্ড
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{ADMIN_USERNAME}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("যেকোনো সাহায্যের জন্য নিচে ক্লিক করুন 👇", reply_markup=reply_markup)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()            InlineKeyboardButton(
                "💬 Contact Admin", 
                url=f"https://t.me/{ADMIN_USERNAME}"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "যেকোনো সাহায্যের জন্য নিচে ক্লিক করুন 👇",
        reply_markup=reply_markup
    )

# মেইন ফাংশন
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
