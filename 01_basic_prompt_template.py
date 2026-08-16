"""
01_basic_prompt_template.py
---------------------------
Concept: Introduction to LangChain's PromptTemplate with variables.

This script demonstrates:
- How to create a dynamic text prompt using `PromptTemplate`.
- How to fill placeholders programmatically.
- How to send the formatted prompt to an LLM and display the result.

Example:
    "Write a short poem about {topic} in {style}."
"""
from langchain_core.prompts import PromptTemplate
from llm_provider import get_llm

# =======================================
# 1️⃣ Create and use a PromptTemplate
# =======================================
prompt_template = PromptTemplate(
    input_variables = ["topic", "style"],
    template = "write a short poem about {topic} in {style}"
)

# =======================================
# 2️⃣ Dynamically fill in variables in prompt
# =======================================
filled_prompt = prompt_template.format(topic = "Machine Learning", style = "gen-z accent")
print("---- Prompt Template Demonstration ----")
print(f"Filled Prompt:\n{filled_prompt}\n")
print("-" * 50)

# =======================================
# 3️⃣ Send prompt to LLM
# =======================================
llm = get_llm()
response = llm.invoke(filled_prompt)

# =======================================
# 4️⃣ Output
# =======================================
print("🤖 Model Response:\n")
print(response.content)
print("-" * 50)