"""
03_few_shot_prompting.py
------------------------
Concept: Teaching the model by example (Few-Shot Prompting)
LangChain Class: FewShotPromptTemplate

This script demonstrates:
- How to teach the model by showing input–output examples (few-shot).
- How to compare results with and without few-shot examples.
- Uses config.json for model settings and .env for API keys.
"""
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from llm_provider import get_llm

# ==========================================
# 1️⃣ Define Few-Shot Examples
# ==========================================
examples = [
    {"movie": "The Shawshank Redemption", "genre": "Genre found -> Drama"},
    {"movie": "The Matrix", "genre": "Genre found -> Sci-fi"},
    {"movie": "The Dark Knight", "genre": "Genre found -> Drama, Action"}
]

# ==========================================
# 2️⃣ Create Few Shot Prompt Template
# ==========================================

# Template for one example
example_prompt = PromptTemplate(
    input_variables = ["movie", "genre"],
    template = "Movie: {movie}\nGenre: {genre}\n"
)

# Create Few Shot Prompt Template
few_shot_prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt = example_prompt,
    suffix = "Movie: {movie}\nGenre:",
    input_variables = ["movie"]
)

# ==========================================
# 3️⃣ Compare with and without Few-Shot Examples
# ==========================================
query = {"movie": "Inception"}
llm = get_llm()

print("🎬 Few-Shot Prompting Demonstration")
print("-----------------------------------")

# ==========================================
# 4️⃣ Without Few-Shot (plain)
# ==========================================
no_fewshot_prompt = f"What genre does the movie '{query['movie']}' belong to?"
print("---- Without Few-Shot (Plain) -----")
print(f"Prompt: {no_fewshot_prompt}")

# =======================================
# 5️⃣ Output without Few-Shot Prompt
# =======================================
print("\n🤖 Model Response: ")
response_plain = llm.invoke(no_fewshot_prompt)
print(response_plain.content)

print("-----------------------------------")
print("-----------------------------------")


# =======================================
# 6️⃣ Dynamically fill in variables in prompt 
# with Few-Shot (examples included)
# =======================================
formatted_prompt = few_shot_prompt.format(**query)
print("\n\n---- With Few-Shot Examples ----")
print(f"Prompt: {formatted_prompt}")
response_fewshot = llm.invoke(formatted_prompt)

# =======================================
# 7️⃣ Output with Few-Shot Prompt
# =======================================
print("\n🤖 Model Response:")
print(response_fewshot.content)



