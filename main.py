from Extract_Specific_Details.main import extract_specific_details
from Generate_topic_keyword.llm_output import generate_topic_keyword
from Generate_Intro.main import generate_intro, refine_intro
from Generate_Guide.main import generate_guide
from Generate_issue_troubleshoot.main import generate_issue_troubleshooting
import asyncio
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

async def main():
    # specific_details = await extract_specific_details()
    # logger.info("Specific details extracted")
    # topic_keyword = await generate_topic_keyword()
    # logger.info("Topic keyword generated")
    # # logger.debug(f"Topic keyword: {topic_keyword}")
    # # logger.debug(f"Specific details: {specific_details}")
    # final_output = {
    #     "topic_keyword": topic_keyword,
    #     "specific_details": specific_details
    # }
    # with open("combined_output1.json", "w") as f:
    #     json.dump(final_output, f, indent=4)
    # logger.info("Final output saved to combined_output1.json")

    # intro = await generate_intro()
    # refined_intro = await refine_intro(intro)
    
    # Guide = await generate_guide()
    issue_troubleshoot = await generate_issue_troubleshooting()



if __name__ == "__main__":
    asyncio.run(main())
