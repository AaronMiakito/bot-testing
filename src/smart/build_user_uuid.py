"""
This module provides a function to construct a unique identifier (UUID) for a user based on the bot's username and the Telegram user's ID.
"""
from telegram.ext import ContextTypes


def build_user_uuid(update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """
    Build a unique user uuid.
    """
    return context.bot.username.lower() + str(update.effective_user.id)
