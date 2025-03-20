# placeholder
from app.core.openai_client import get_completion


async def generate_openai_response(prompt: str) -> str:
    return await get_completion(prompt)
