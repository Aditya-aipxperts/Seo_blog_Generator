import asyncio
import json
from setup_env import setup_environment, get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

from ask_ai import keywords

async def main():
    with open("/home/aip-63/Desktop/Seo_Blog_Generator/transcript.txt", "r") as f:
        transcript = f.read()

    extracted_data = await keywords(transcript,llm)

    with open("raw_output.json","w") as f:
        json.dump(extracted_data,f, indent=4)

    print("✅ Extracted details saved to raw_output.json")


if __name__ == "__main__":
    asyncio.run(main())