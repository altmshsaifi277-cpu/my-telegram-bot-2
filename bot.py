from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = "9064894809:AAFHZI6dPcum2ZoCst8__ZGV8KHWobYQ7vE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✨ Get exclusive access to premium content\n"
        "💰 Affordable plans starting at just ₹99\n"
        "✨ Content quality aisi ki dekhi nahi hogi\n"
        "✨ Only Premium Content\n"
        "✨ Daily New Uploads\n"
        "✨ Cp, Rp, Indian, Foreign, Dark everything\n"
        "✨ 10000+ Cp videos\n"
        "✨ 25000+ Rp videos\n"
        "✨ M0m S0n 5k Videos\n\n"
        "✨ TRY OUR ANY PLAN FOR CHECKING THE QUALITY ✨"
    )

    keyboard = [
        [InlineKeyboardButton("⚡ ANIMAL FUN ⚡ ₹49/30 DAYS", callback_data="plan_1")],
        [InlineKeyboardButton("🥵 CHILD CARN PACK ⚡ ₹59/30 DAYS", callback_data="plan_2")],
        [InlineKeyboardButton("🥵 CHILD CORN 💧 ₹119/50 DAYS", callback_data="plan_3")],
        [InlineKeyboardButton("🥵 REAL INDIAN DESI POM 💯 ₹79/30 DAYS", callback_data="plan_4")],
        [InlineKeyboardButton("🥵 R@PE FULL VIDEO 🔥 ₹99/30 DAYS", callback_data="plan_5")],
        [InlineKeyboardButton("🥵 BAAP BETI ⚡ ₹59/30 DAYS", callback_data="plan_6")],
        [InlineKeyboardButton("🥵 ALL GROUP VIDEOS ❤️ ₹149/LIFETIME", callback_data="plan_7")],
        [InlineKeyboardButton("🔥 ALL GROUP FULL ACCESS 💯 ₹179/LIFETIME", callback_data="plan_8")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hello Nox\n\nChoose a plan to get started", reply_markup=reply_markup)
    await update.message.reply_text(text)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Aapne select kiya: {query.data}. Payment karne ke liye yahan UPI ID par pay karein: yourname@paytm")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
