from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama",
)

response = client.chat.completions.create(
    model="mistral",
    messages=[
        {"role": "system", "content": "Tu es un chef cuisinier français avec 10 ans d'expérience."},
        {"role": "user", "content": "Présentes un plat typiquee français"}
    ]
)

print(response.choices[0].message.content)