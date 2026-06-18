RELEVANCE_ASSESSMENT_SYSTEM_PROMPT = """
You are an expert NIH scientific reviewer. Your task is to assess how relevant a given
scientific topic is to a target research direction or problem statement.

Your evaluation must be:
- Objective
- High‑level
- Based on scientific alignment, not writing style
- Focused on conceptual fit, not implementation details

Return a JSON object with:
- "relevance_score": an integer from 1 to 5
- "justification": a 2–3 sentence explanation of the score
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os

def build_relevance_assessment_chain(model_name="gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", RELEVANCE_ASSESSMENT_SYSTEM_PROMPT),
            ("human",
             "Evaluate the relevance of the following topic to the target research direction.\n\n"
             "Topic: {{ topic }}\n\n"
             "Target Research Direction: {{ target }}")
        ],
        template_format="jinja2"
    )

    parser = JsonOutputParser()

    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        base_url=os.environ.get("OPENAI_API_BASE")
    )

    chain = prompt | llm | parser
    return chain

def assess_relevance(topic: str, target: str, model_name="gpt-4o-mini"):
    chain = build_relevance_assessment_chain(model_name=model_name)
    return chain.invoke({"topic": topic, "target": target})
