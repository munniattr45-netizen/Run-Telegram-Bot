import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Secrets থেকে BOT_TOKEN পড়বে
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = "RASEL_B_D_T_148589"
ADMIN_USERNAME = "RASEL_B_D_T_148589"
MINI_APP_URL = "t.me/Ai_hackbdtbot/curiousbombolonee31880"

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗔𝗶 𝗛𝗔𝗖𝗞 𝗕𝗢𝗧

আমাদের 𝗔𝗶 𝗛𝗔𝗖𝗞 𝗕𝗢𝗧 এর মাধ্যমে সিগন্যাল নিয়ে প্রতিদিন ফ্রিতে ৫০০-১০০০ হাজার টাকা প্রফিট করতে পারবেন।

🟩𝐏𝐔𝐁𝐋𝐈𝐂 𝐕𝐈𝐏 𝐒𝐈𝐆𝐍𝐀𝐋 𝐆𝐑𝐎𝐔𝐏🟩
@My_Personal_Time_Free_Live_Class
@My_Personal_Time_Free_Live_Class

➡️𝗔𝗶 𝗛𝗔𝗖𝗞 𝗕𝗢𝗧 𝙇𝙄𝙉𝙆:⬇️
t.me/Ai_hackbdtbot/curiousbombolonee31880
t.me/Ai_hackbdtbot/curiousbombolonee31880

➡️𝙍𝙀𝙂𝙄𝙎𝙏𝙍𝘼𝙏𝙄𝙊𝙉 𝙇𝙄𝙉𝙆:⬇️
https://www.hgzy32.com/#/register?invitationCode=73242148589

ডিপোজিট করলে পাচ্ছেন Cash Back offer
▶️ডিপোজিট-300- বোনাস-  200৳🆗
▶️ডিপোজিট-500- বোনাস-  280৳🆗
▶️ডিপোজিট-1000-বোনাস- 440৳🆗
▶️ডিপোজিট-5000-বোনাস- 1250৳🆗

বোনাসের জন্য 𝗢𝗪𝗡𝗘𝗥 𝗜𝗗 তে মেসেজ দেন 💬
@RASEL_B_D_T_148589
@RASEL_B_D_T_148589
"""
    keyboard = [
        [InlineKeyboardButton("🎁 Owner Contact", url=f"https://t.me/{OWNER_USERNAME}")],
        [InlineKeyboardButton("🤖 Ai Hack Bot", url=MINI_APP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)

# /help কমান্ড
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{ADMIN_USERNAME}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("যেকোনো সাহায্যের জন্য নিচে ক্লিক করুন 👇", reply_markup=reply_markup)

# মেইন ফাংশন
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
