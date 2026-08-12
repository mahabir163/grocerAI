from groq import Groq
import json
import os
from django.conf import settings
# Recommended: Store your API key in an environment variable
# set GROQ_API_KEY=your_api_key   (Windows)
# export GROQ_API_KEY=your_api_key (Linux/macOS)

client = Groq(
    api_key= settings.OPENAI_API_KEY
)


def extract_products(text):
    prompt = f"""
You are an AI that extracts grocery products from shopping bills.

Extract every grocery item.

Ignore:
- Shop name
- GST
- Address
- Phone number
- Invoice number
- Cashier
- Total amount
- Tax

Return ONLY valid JSON.

Format:

[
  {{
    "name": "",
    "quantity": 1
  }}
]

Bill:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a grocery bill parser. Always return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
    )

    result = response.choices[0].message.content.strip()

    # Remove markdown if returned
    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)