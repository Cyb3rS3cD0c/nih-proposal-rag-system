from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os

AIMS_SYSTEM_PROMPT = """
You are an expert NIH grant writer. Given a set of research ideas,
draft 2–3 NIH-style Specific Aims.
Return JSON:
- "aims": [ {"title": "...", "description": "..."} ]
"""

def build_aims_chain(model_name="gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", AIMS_SYSTEM_PROMPT),
            ("human", "Research Ideas:\n{{ ideas }}")
        ],
        template_format="jinja2"
    )

    parser = JsonOutputParser()
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        base_url=os.environ.get("OPENAI_API_BASE")
    )

    return prompt | llm | parser

def generate_specific_aims(ideas_output, model_name="gpt-4o-mini"):
    chain = build_aims_chain(model_name=model_name)
    ideas_str = "\n".join(
        f"- {i['title']}: {i['rationale']}" for i in ideas_output.get("ideas", [])
    )
    return chain.invoke({"ideas": ideas_str})