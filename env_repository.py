"""
Set the environment variables consistently for security.
"""
import os
from dotenv import load_dotenv

load_dotenv()

AI_MACHINE_URL = os.getenv("AI_MACHINE_URL")
AI_MACHINE_TIMEOUT = int(os.getenv("AI_MACHINE_TIMEOUT"))
