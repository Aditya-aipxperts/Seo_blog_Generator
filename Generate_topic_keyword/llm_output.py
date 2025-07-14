import asyncio
import json
import re
from setup_env import setup_environment, get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

from Generate_topic_keyword.ask_ai import keywords
# from ask_ai import keywords

async def generate_topic_keyword():
    with open("/home/aip-63/Desktop/Seo_Blog_Generator/transcript.txt", "r") as f:
        transcript = f.read()

    extracted_data = await keywords(transcript,llm)
    print(extracted_data)
    extracted_data = extracted_data.strip()
    extracted_data = re.sub(r'\s+', ' ', extracted_data).strip()
    if extracted_data.startswith("```json"):
        extracted_data = extracted_data.split("```json")[1].split("```")[0]
    if extracted_data.startswith("```"):
        extracted_data = extracted_data.split("```")[1]
    if extracted_data.endswith("```"):
        extracted_data = extracted_data.split("```")[0]
    if extracted_data.startswith("```json"):
        extracted_data = extracted_data.split("```json")[1].split("```")[0]

    data = json.loads(extracted_data)
    with open("extracted.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("✅ Extracted details saved to extracted.json")
    return data


if __name__ == "__main__":
    asyncio.run(generate_topic_keyword())