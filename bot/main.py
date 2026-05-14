import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

from backend.meta import get_meta

TOKEN = os.getenv("BOT_TOKEN")

meta_cache = []

async def meta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global meta_cache
    meta_cache = get_meta()

    keyboard = []
    for i, comp in enumerate(meta_cache):
        keyboard.append([
            InlineKeyboardButton(
                f"{comp['tier']} - {comp['name']}",
                callback_data=str(i)
            )
        ])

    await update.message.reply_text(
        "🔥 META TFT (AUTO)",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    comp = meta_cache[int(query.data)]

    text = f"""
🔥 {comp['name']} ({comp['tier']})

🧠 Units: {', '.join(comp['units'])}
⚔️ Items: {', '.join(comp['items'])}
💎 Augments: {', '.join(comp['augments'])}
"""

    if comp["image"]:
        await query.message.reply_photo(photo=comp["image"], caption=text)
    else:
        await query.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("meta", meta))
app.add_handler(CallbackQueryHandler(detail))

app.run_polling()