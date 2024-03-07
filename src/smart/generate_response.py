"""
Generates AI-based responses to user messages using asynchronous HTTP requests.
"""
import json
import aiohttp
import env_repository as env


INVOKE_URL = env.AI_MACHINE_URL + "/invoke_v2"


async def generate_response(user_message, user_uuid) -> None:
    """
    Generate a response using the AI Machine.
    """
    with open('src/smart/config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    print(config, flush=True)


    if isinstance(config["mission"], list):
        config["mission"] = ' '.join(config["mission"])
    async with aiohttp.ClientSession() as session:
        async with session.post(
            INVOKE_URL,
            json={
                "user_input": user_message,
                "user_uuid": user_uuid,
                **config,
            },
            timeout=env.AI_MACHINE_TIMEOUT,
        ) as response:
            response_json = await response.json()
            ai_response = response_json.get("output")
            return ai_response
