from Fetch_transcript.main import extract_video_id, get_transcript_with_backoff
from Extract_Specific_Details.main import extract_specific_details
from Generate_topic_keyword.llm_output import generate_topic_keyword
from Generate_Intro.main import generate_intro, refine_intro
from Generate_Guide.main import generate_guide
from Generate_issue_troubleshoot.main import generate_issue_troubleshooting
from Generate_Conclusion.main import generate_conclusion
from Generate_CTA.main import generate_cta
from Generate_Customization_tips.main import generate_customization_tips
from Domain_aligned.main import domain_aligned
from Rewrite_Blog.main import rewrite_blog
import asyncio
import json
import logging
import traceback

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
    video_url = input("Enter the YouTube video URL: ")
    Domain_url = input("Enter your Domain URL: ")
    Raw_blog = input("Enter the raw blog: ")
    try:
        video_id = extract_video_id(video_url)
        print(f"✅ Video ID: {video_id}")
        transcript = get_transcript_with_backoff(video_id)
        if not transcript or "Failed after multiple retries" in transcript:
            print(f"⚠️  Transcript not available for: {video_url}")
        else:
            print("Transcript Fetched")
            print(transcript)
            print("------------------------------------------------------------")
    except Exception as e:
        print("❌ Error:", e)
        traceback.print_exc()

    specific_details = await extract_specific_details(transcript)
    logger.info("Specific details extracted")
    topic_keyword = await generate_topic_keyword(transcript)
    logger.info("Topic keyword generated")
    combined_data1 = {
        "topic_keyword": topic_keyword,
        "specific_details": specific_details
    }
    with open("combined_data1.json", "w") as f:
        json.dump(combined_data1, f, indent=4)
    logger.info("Final output saved to combined_data1.json")

    intro = await generate_intro()
    refined_intro = await refine_intro(intro)
    
    Guide = await generate_guide()
    issue_troubleshoot = await generate_issue_troubleshooting()

    Conclusion = await generate_conclusion()

    CTA = await generate_cta()

    customization_tips = await generate_customization_tips()

    combined_data2 = {
        "Introduction" : refined_intro,
        "Guide" : Guide,
        "Issue_Troubleshoot" : issue_troubleshoot,
        "Conclusion" : Conclusion,
        "CTA" : CTA,
        "Customization_tips" : customization_tips
    }

    with open("combined_data2.json","w",encoding="utf-8") as f:
        json.dump(combined_data2, f, indent=4)
    logger.info("Final output saved to combined_data2.json")

    Domain_aligned = await domain_aligned(Domain_url, transcript)
    Blog = await rewrite_blog(Raw_blog)
    logger.info("Blog saved to FINAL_BLOG.json")
if __name__ == "__main__":
    asyncio.run(main())
