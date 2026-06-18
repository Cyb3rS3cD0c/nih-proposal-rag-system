from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI


# -----------------------------
# SYSTEM PROMPT
# -----------------------------
TOPIC_EXTRACTION_SYSTEM_PROMPT = """
You are an expert NIH research assistant. Your task is to extract the core scientific topics
from a bundle of research papers. These topics must be:

- High‑level scientific themes
- Not tied to any single paper
- Not overly specific
- Not NIH‑proposal language (no aims, no hypotheses)
- Suitable as conceptual building blocks for later proposal development

Return ONLY a JSON object with a top-level key called "topics".
Each topic must contain:
- "name": a short topic name
- "description": a 1–2 sentence description
"""

# -----------------------------
# RUNNABLE
# -----------------------------
def build_topic_extraction_chain(model_name="gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", TOPIC_EXTRACTION_SYSTEM_PROMPT),
            ("human", "Extract high‑level scientific topics from the following text:\n\n{{ input_text }}")
        ],
        template_format="jinja2"
    )

    parser = JsonOutputParser()

    import os
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        base_url = os.getenv("OPENAI_API_BASE")
    )

    chain = prompt | llm | parser
    return chain

# -----------------------------
# PUBLIC FUNCTION
# -----------------------------
def extract_topics(text: str, model_name="gpt-4o-mini"):
    chain = build_topic_extraction_chain(model_name=model_name)
    return chain.invoke({"input_text": text})