"""Ce module gère la réponse aux messages vocaux des utilisateurs en utilisant l'API d'OpenAI."""
import time
from pathlib import Path

from telegram import Update
from telegram.ext import ContextTypes

import openai

from src.smart.build_user_uuid import build_user_uuid
from src.smart.generate_response import generate_response
from src.smart.send_message import send_message

# Le reste du code reste inchangé...


async def respond_to_user_voice(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    Generate a response when the user sends a voice message.
    First, the voice message is converted to text using OpenAI's API.
    Then, the text message is sent to the AI Machine.
    """

    ai_response = "Désolé, aucune réponse n'a pu être générée.\n Réessayez dans quelques minutes !"

    try:
        voice_file = await context.bot.get_file(update.message.voice.file_id)
        voice_file_name = f"{update.effective_user.id}_{int(time.time())}.ogg"
        await voice_file.download_to_drive(voice_file_name)
        speech_file_path = Path(voice_file_name)
        print(speech_file_path, flush=True)
        transcription = openai.audio.transcriptions.create(
            model="whisper-1", file=speech_file_path
        )

        user_message = (
            "[info: retranscription vocale. pense à confirmer les orthographes des noms propres si besoin.]\n"
            + transcription.text
        )

        print(user_message, flush=True)

        user_uuid = build_user_uuid(update, context)
        ai_response = await generate_response(user_message, user_uuid)
    # pylint: disable=broad-except
    except Exception as e:
        print(f"Request failed: {e}", flush=True)
        ai_response = "Désolé, aucune réponse n'a pu être générée.\n Réessayez dans quelques minutes !"

    finally:
        # await asyncio.sleep(20)
        await send_message(update, ai_response)
