"""
Manages AI response creation for user messages.
"""
from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
async def send_message(update, message):
    """
    Tenacity wrapper for sending a message.
    """
    await update.message.reply_text(message, parse_mode="Markdown")
