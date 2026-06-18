from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


def generate_ideas(ranked_topics, gaps):
    """
    Generate research ideas based on ranked topics and identified gaps.
    """

    system_prompt = """
    You are an NIH proposal strategist. Generate research ideas based on ranked topics
    and conceptual gaps. Return JSON with an 'ideas' list.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Ranked topics: {topics}\nGaps: {gaps}")
    ])

    parser = JsonOutputParser()
    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = prompt | llm | parser

    return chain.invoke({
        "topics": ranked_topics,
        "gaps": gaps
    })