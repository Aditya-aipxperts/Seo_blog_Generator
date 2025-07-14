from Generate_topic_keyword.utils.prompts import KEYWORDS_PROMPT

async def  keywords(transcipt:str, llm) -> str:
    response = await llm.ainvoke(KEYWORDS_PROMPT + "\n\n" + transcipt)
    return response.content.strip()

