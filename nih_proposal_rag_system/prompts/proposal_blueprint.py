from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os

BLUEPRINT_SYSTEM_PROMPT = """
You are an NIH proposal architect. Given Specific Aims,
produce a structured proposal blueprint with sections:
- Significance
- Innovation
- Approach (per Aim)
Return JSON:
- "blueprint": {
    "significance": "...",
    "innovation": "...",
    "approach": [ {"aim": "...", "plan": "..."} ]
  }
"""

def build_blueprint_chain(model_name="gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", BLUEPRINT_SYSTEM_PROMPT),
            ("human", "Specific Aims:\n{{ aims }}")
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

def generate_proposal_blueprint(aims_output, model_name="gpt-4o-mini"):
    chain = build_blueprint_chain(model_name=model_name)
    aims_str = "\n".join(
        f"- {a['title']}: {a['description']}" for a in aims_output.get("aims", [])
    )
    return chain.invoke({"aims": aims_str})