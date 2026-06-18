from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os

POLISH_SYSTEM_PROMPT = """
You are an expert NIH grant writer. Given a draft proposal,
polish the language, tighten the logic, and ensure NIH-style clarity.
Return a single polished text.
"""

def build_polisher_chain(model_name="gpt-4o-mini", temperature=0.2):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", POLISH_SYSTEM_PROMPT),
            ("human", "{{ draft }}"),
        ],
        template_format="jinja2",
    )

    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        base_url=os.environ.get("OPENAI_API_BASE"),
    )

    return prompt | llm | StrOutputParser()

def polish_proposal(draft_text, model_name="gpt-4o-mini", temperature=0.2):
    chain = build_polisher_chain(model_name=model_name, temperature=temperature)
    return chain.invoke({"draft": draft_text})