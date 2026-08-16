"""
02_chat_prompt_template.py
---------------------------
Concept: Role-based structured messages using LangChain's ChatPromptTemplate.

This script demonstrates:
- How to define structured messages for system, user, and assistant roles.
- How to include placeholders for dynamic user input.
- How to send the assembled chat prompt to a chat model (OpenAI or Gemini).
"""
from langchain_core.prompts import ChatPromptTemplate
from llm_provider import get_llm

# =======================================
# 1️⃣ Create and use a ChatPromptTemplate
# =======================================
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative assistant who writes in a friendly tone"),
    ("user", "Write a short greeting message for someone who just started learning {subject}")
])

# =======================================
# 2️⃣ Dynamically fill in variables in prompt
# =======================================
filled_prompt = chat_prompt.format_messages(subject = "Transformers")
print("---- ChatPromptTemplate Demonstration ----")
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