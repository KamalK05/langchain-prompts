"""
04_chain_of_thought_prompting.py
--------------------------------
Concept: Encouraging reasoning steps (Chain-of-Thought prompting).
LangChain Pattern: Explicit reasoning cue in template.

👉🏽 When to use CoT:
Use CoT when the problem requires multiple reasoning steps or logical deduction to reach the answer.

> Normal Prompting (BAD for this):
---
Q: A store buys 15 apples for $30 and sells them for $3 each. 
How much profit do they make?

A: $15
---
❌ The model might guess incorrectly or make a mistake

👉🏽 Chain-of-Thought Prompting (GOOD for the same question):

A: Let's think step by step:
1. Cost per apple = $30 ÷ 15 = $2 per apple
2. Selling price per apple = $3
3. Profit per apple = $3 - $2 = $1
4. Total profit = 15 apples × $1 = $15

So the answer is $15.

✅ Forces the model to show its work, leading to correct answer


---
Use NORMAL prompting for:
Simple factual questions
Classification tasks
Straightforward extraction
Example: "What's the capital of France?" → "Paris"

Use CoT prompting for:
Math problems
Logical puzzles
Multi-step reasoning
Complex decision making
Example: Medical diagnosis reasoning, legal analysis, science problems
---
"""
from langchain_core.prompts import PromptTemplate
from llm_provider import get_llm

# ==========================================
# 1️⃣ Define Templates
# ==========================================
direct_template = PromptTemplate(
    input_variables = ["question"],
    template = "{question}"
)

cot_template = PromptTemplate(
    input_variables = ["question"],
    template = (
            "Let`s think step by step before answering.\n"
            "{question}\n"
            "Now give the final concise answer."
        )
)

llm = get_llm()

# ==========================================
# 2️⃣ Test Questions (math / logic)
# ==========================================
questions = [
    # classic cognitive reflection test (often benefits from step-by-step)
    "If a bat and a ball cost $1.10 in total and the bat costs $1.00 more than the ball, how much does the ball cost?",
    # proportional reasoning example
    "If 5 machines take 5 minutes to make 5 widgets, how long will 100 machines take to make 100 widgets?"
]

# ==========================================
# 2️⃣ Run and Print Method
# ==========================================
def run_and_print(formatted_prompt: str, llm):
    """Invoke the LLM and return the raw textual response (with basic error handling)."""
    try:
        response = llm.invoke(formatted_prompt)
        if hasattr(response, "content"):
            return response.content
        else:
            return str(response)
    except Exception as e:
        return f"[Invocation Error] {e}"

# ==========================================
# 3️⃣ Demo
# ==========================================
print("🧭 Chain-of-Thought Prompting Demo")
print("---------------------------------\n")

for i, q in enumerate(questions, start = 1):
    print(f"==== Question {i} =====\n")
    print(f"Q: {q}\n")

    # ==========================================
    # 3️⃣.1️⃣ Direct / zero-shot Prompt
    # ==========================================
    direct_prompt = direct_template.format(question = q)
    print(f"⋊ Direct Prompt Sent: {direct_prompt}")
    print("\nModel Response (Direct): \n")
    direct_response = run_and_print(direct_prompt, llm)
    print(direct_response)
    print("\n" + "-" * 40 + "\n")

    # ==========================================
    # 3️⃣.2️⃣ Chain-of-thought (CoT) Prompt
    # ==========================================
    cot_prompt = cot_template.format(question = q)
    print(f"🔗 Chain-of-Thought Prompt Sent: {cot_prompt}")
    cot_response = run_and_print(cot_prompt, llm)
    print("\nModel Response (Chain-of-Thought): \n")
    print(cot_response)
    print("\n" + "=" * 80 + "\n")
