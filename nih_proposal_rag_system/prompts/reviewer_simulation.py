from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os

REVIEW_SYSTEM_PROMPT = """
You are simulating an NIH study section reviewer.
Given a proposal, provide:
- strengths
- weaknesses
- overall impact score (1–9)
Return JSON:
- "strengths": [...]
- "weaknesses": [...]
- "impact_score": int
"""

def build_reviewer_chain(model_name="gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", REVIEW_SYSTEM_PROMPT),
            ("human", "{{ proposal }}"),
        ],
        template_format="jinja2",
    )

    parser = JsonOutputParser()
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        base_url=os.environ.get("OPENAI_API_BASE"),
    )

    return prompt | llm | parser

def simulate_reviewer(proposal_text, model_name="gpt-4o-mini"):
    chain = build_reviewer_chain(model_name=model_name)
    return chain.invoke({"proposal": proposal_text})