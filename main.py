from Extract_Specific_Details.main import extract_specific_details
from Generate_topic_keyword.llm_output_parser import parse_keywords_output_main
import asyncio
import json

async def main():
    specific_details = await extract_specific_details()
    topic_keyword = await parse_keywords_output_main()
    print(topic_keyword)
    print(specific_details)
    final_output = {
        "topic_keyword": topic_keyword,
        "specific_details": specific_details
    }
    print(final_output)
    with open("combined_output1.json", "w") as f:
        json.dump(final_output, f, indent=4)
    print("✅ Final output saved to combined_output1.json")

if __name__ == "__main__":
    asyncio.run(main())