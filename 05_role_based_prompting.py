"""
05_role_based_prompting.py
--------------------
Concept: Persona-driven prompting
LangChain Class: ChatPromptTemplate

This script demonstrates:
- How to define different personas via the system role.
- How to ask the same question under different roles and compare the tone/vocabulary.
- Uses config.json for model settings and .env for API keys.
"""
from langchain_core.prompts import ChatPromptTemplate
from llm_provider import get_llm

# ==========================================
# 1️⃣ Define Personas via System Role
# ==========================================
personas = {
    "Teacher": "You are a patient and knowledgeable teacher who explains concepts clearly with examples.",
    "Lawyer": "You are an analytical corporate lawyer. Respond with precision & logic. Try to connect things with law/legal domain.",
    "Coder": "You are a seasoned software developer who explains things using technical analogies and software relevance.",
    "Finance Expert": "You are a finance professional who connects technical concepts to markets and investments."
}

# ==========================================
# 2️⃣ Define Query
# ==========================================
question = "Explain blockchain technology in short & simple terms."

# ==========================================
# 3️⃣ ChatPromptTemplate with Persona
# ==========================================
def create_template_and_prompt(persona_description: str, question: str):
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", persona_description),
        ("user", "{question}")
    ])

    filled_prompt = chat_prompt.format_messages(question = question)
    return filled_prompt

# ==========================================
# 4️⃣ Run Demo
# ==========================================   
def main():
    print("🧠 Role / Persona Prompting Demonstration ")
    print("-----------------------------------------")
    print(f"Question: {question}\n")

    for role, persona_description in personas.items():
        # ==========================================
        # 4️⃣.1️⃣ Print Persona Being Tested
        # ========================================== 
        print(f"👤 Persona: {role}")
        print("-" * (20 + len(role)))
        print(f"🔹 System Role Prompt: {persona_description}")

        # ==========================================
        # 4️⃣.2️⃣ Invoke LLM
        # ========================================== 
        filled_prompt = create_template_and_prompt(persona_description, question)
        llm = get_llm()
        response = llm.invoke(filled_prompt)
        print("\n🤖 Model Response: \n")
        print(response.content)
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()