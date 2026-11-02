import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TOKEN = "9064894809:AAFHZI6dPcum2ZoCst8__ZGV8KHWobYQ7vE"
UPI_ID = "altamas001@fam"
# Tera QR code ka direct image link
QR_IMAGE_URL = "https://i.ibb.co/6yq4W5g/1000038297.jpg"

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
        [InlineKeyboardButton("⚡ ANIMAL FUN ⚡ ₹49/30 DAYS", callback_data="plan_49")],
        [InlineKeyboardButton("🥵 CHILD CARN PACK ⚡ ₹59/30 DAYS", callback_data="plan_59")],
        [InlineKeyboardButton("🥵 CHILD CORN 💧 ₹119/50 DAYS", callback_data="plan_119")],
        [InlineKeyboardButton("🥵 REAL INDIAN DESI POM 💯 ₹79/30 DAYS", callback_data="plan_79")],
        [InlineKeyboardButton("🥵 R@PE FULL VIDEO 🔥 ₹99/30 DAYS", callback_data="plan_99")],
        [InlineKeyboardButton("🥵 BAAP BETI ⚡ ₹59/30 DAYS", callback_data="plan_59_bb")],
        [InlineKeyboardButton("🥵 ALL GROUP VIDEOS ❤️ ₹149/LIFETIME", callback_data="plan_149")],
        [InlineKeyboardButton("🔥 ALL GROUP FULL ACCESS 💯 ₹179/LIFETIME", callback_data="plan_179")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hello Nox\n\nChoose a plan to get started", reply_markup=reply_markup)
    await update.message.reply_text(text)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    
