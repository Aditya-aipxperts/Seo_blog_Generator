from Fetch_transcript.main import extract_channel_id, get_video_ids, get_transcript_with_backoff
from Extract_Specific_Details.main import extract_specific_details
from Generate_topic_keyword.llm_output import generate_topic_keyword
from Generate_Intro.main import generate_intro, refine_intro
from Generate_Guide.main import generate_guide
from Generate_issue_troubleshoot.main import generate_issue_troubleshooting
from Generate_Conclusion.main import generate_conclusion
from Generate_CTA.main import generate_cta
from Generate_Customization_tips.main import generate_customization_tips
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
    channel_url = input("Enter the YouTube channel URL: ")
    try:
        channel_id = extract_channel_id(channel_url)
        print(f"✅ Channel ID: {channel_id}")

        videos = get_video_ids(channel_id, max_results=1)
        print(f"📹 Found {len(videos)} videos")

        for idx, video in enumerate(videos, start=1):
            print(f"\n=== Transcript for Video {idx}: {video['title']} ===")
            transcript = get_transcript_with_backoff(video["videoId"])
            if not transcript or "Failed after multiple retries" in transcript:
                print(f"⚠️  Transcript not available for: {video['title']}")
            print("Transcript Fetched")  
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

if __name__ == "__main__":
    asyncio.run(main())
