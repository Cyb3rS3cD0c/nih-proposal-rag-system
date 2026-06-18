from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


def identify_gaps(ranked_topics, target_direction: str):
    """
    Identify conceptual gaps based on ranked topics and target direction.
    """

    system_prompt = """
    You are an NIH proposal strategist. Identify conceptual gaps between the ranked topics
    and the target research direction. Return JSON with a 'gaps' list.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Ranked topics: {topics}\nTarget direction: {target}")
    ])

    parser = JsonOutputParser()

    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = prompt | llm | parser

    return chain.invoke({
        "topics": ranked_topics,
        "target": target_direction
    })