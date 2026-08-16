"""
08b_load_and_run_prompt_yaml.py
-------------------------------
Concept: External prompt versioning and reusability.
LangChain Function: load_prompt

This script demonstrates:
- How to load a prompt from an external YAML file.
- How to format it dynamically with variables.
- How to send it to an LLM (OpenAI or Gemini) for response generation.

Example Use Case:
Reusing the 'blog writer' prompt with different topics and tones.
"""
from langchain_core.prompts import load_prompt
from llm_provider import get_llm

# ==========================================
# 1️⃣ Load and Run Prompt
# ==========================================
prompt_path = "08_prompt_reuse_yaml/blog_prompt.yaml"
prompt = load_prompt(prompt_path)

# ==========================================
# 2️⃣ Example Topics
# ==========================================
topics = [
    {"topic": "Artificial Intelligence in Education", "audience": "teachers", "tone": "inspirational"},
    {"topic": "Healthy Remote Work Habits", "audience": "freelancers", "tone": "friendly"}
]


# ==========================================
# 3️⃣ Run Demo
# ==========================================
def main():
    print("🧩 YAML Prompt Reuse Demonstration")
    print("----------------------------------")
    print(f"Loaded Prompt from: {prompt_path}\n")

    for i, vars in enumerate(topics, start=1):
        print(f"📝 Example {i}:")
        print(f"📌 Topic: {vars['topic'].capitalize()}")
        print(f"👤 Audience: {vars['audience'].capitalize()}")
        print(f"🎤 Tone: {vars['tone'].capitalize()}\n")

        # Format the YAML prompt dynamically
        formatted_prompt = prompt.format(**vars)
        print("🔹 Formatted Prompt Sent to Model:\n")
        print(formatted_prompt)

        llm = get_llm()
        response = llm.invoke(formatted_prompt)

        print("\n🤖 Model Response:\n")
        print(response.content)
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()
