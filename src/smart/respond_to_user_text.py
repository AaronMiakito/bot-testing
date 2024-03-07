"""
Handles asynchronous generation of AI responses to user messages.
"""
from telegram import Update
from telegram.ext import ContextTypes
from src.smart.build_user_uuid import build_user_uuid
from src.smart.generate_response import generate_response
from src.smart.send_message import send_message


async def respond_to_user_text(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Generate a response when the user sends a text message.
    """
    user_message = update.message.text
    user_uuid = build_user_uuid(update, context)

    response_message = "Désolé, aucune réponse n'a pu être générée.\n Réessayez dans quelques minutes !"

    try:
        print(f"Request received: {user_message}", flush=True)
        response_message = await generate_response(user_message, user_uuid)
        print(f"Response generated: {response_message}", flush=True)

    # pylint: disable=broad-except
    except Exception as e:
        print(f"Request failed: {e}", flush=True)
        response_message = "Désolé, aucune réponse n'a pu être générée.\n Réessayez dans quelques minutes !"
    finally:
        # await asyncio.sleep(20)
        await send_message(update, response_message)
