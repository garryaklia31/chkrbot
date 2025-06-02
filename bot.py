
import os
import logging
from telegram import Update, Document
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from email_checker import check_emails_from_file

TELEGRAM_BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a .txt file containing Gmail addresses (one per line).")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document: Document = update.message.document

    if not document.file_name.endswith(".txt"):
        await update.message.reply_text("Please send a .txt file.")
        return

    file_path = f"/tmp/{document.file_name}"
    await document.get_file().download_to_drive(file_path)
    await update.message.reply_text("Checking emails, please wait...")

    result_text = check_emails_from_file(file_path)

    if len(result_text) > 4000:
        with open("/tmp/result.txt", "w") as f:
            f.write(result_text)
        await update.message.reply_document(document=open("/tmp/result.txt", "rb"))
    else:
        await update.message.reply_text(result_text)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    app.run_polling()

if __name__ == "__main__":
    main()
