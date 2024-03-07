"""
Entry point for the Telegram bot.
"""
# pylint: disable=unused-argument
import os
import logging

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from src.smart.respond_to_user_text import respond_to_user_text
from src.openai.respond_to_user_voice import respond_to_user_voice

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


load_dotenv()


print("Starting the bot...", flush=True)
app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

app.add_handler(MessageHandler(
    filters.TEXT, respond_to_user_text, block=False))
app.add_handler(MessageHandler(
    filters.VOICE, respond_to_user_voice, block=False))

# Start the bot. We drop pending updates to avoid spamming the machine with old messages.
app.run_polling(drop_pending_updates=True)
