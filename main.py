import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

PACKAGES = {
    "15 stars": "3 500 сум",
    "25 stars": "6 000 сум",
    "50 stars": "12 000 сум",
    "100 stars": "22 000 сум",
    "200 stars": "45 000 сум",
    "500 stars": "110 000 сум",
    "1k stars": "220 000 сум"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[pkg] for pkg in PACKAGES]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет! Выберите пакет звёзд ⭐️:", reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in PACKAGES:
        price = PACKAGES[text]
        response = (
            f"💫 Вы выбрали: *{text}*\n"
            f"💰 Цена: *{price}*\n\n"
            f"Оплатите на карту и отправьте скрин:\n"
            f"📇 *Humo:* 9860 1606 4754 9924\n"
            f"📇 *UzCard:* 8600 0604 7194 2392\n\n"
            f"После оплаты отправьте скрин сюда или напишите: @sha_xaaa"
        )
        await update.message.reply_markdown(response)
    else:
        await update.message.reply_text("Пожалуйста, выберите пакет звёзд из списка.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
