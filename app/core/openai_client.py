# placeholder
import openai
from app.core.config import settings

openai.api_key = settings.openai_api_key


async def get_completion(prompt: str, model="gpt-4"):
    response = await openai.ChatCompletion.acreate(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message["content"]
