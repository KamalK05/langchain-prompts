"""
06_structured_output_prompting.py
---------------------------------
Concept: Enforcing structured responses
LangChain Classes: ResponseSchema, StructuredOutputParser

This script demonstrates:
- How to define a structured schema for model outputs.
- How to use ResponseSchema + StructuredOutputParser to guide LLMs.
- How to parse and print JSON-like structured data from natural text.

Example Use Case:
Extract key details (title, summary, sentiment, rating) from a customer review.
"""
import json
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from llm_provider import get_llm

# ==========================================
# 1️⃣ Define output schema (Pydantic)
# ==========================================
class ReviewAnalysis(BaseModel):
    '''
    This creates a blueprint for how the AI's response should look.
    > BaseModel = Pydantic's way of saying "this is a structured data template"
    > title/summary/sentiment = The 3 pieces of info you want extracted
    > Field(description=...) = Tells the AI what each field means

    Think of it as a form with 3 empty fields that the AI must fill:

    > Field <---> What goes there
    > title  <--->  Short headline (like "Galaxy X Camera Impresses")
    > summary  <--->  2-3 sentence recap of what customer said
    > sentiment  <--->  Positive/Negative/Neutral
    > rating  <--->  Overall Rating between 1~5
    '''
    title : str = Field(
        description = "A short descriptive title summarizing the review content."
    ),
    description: str = Field(
        description = "A concise 2-3 sentence summary of the customer's opinion."
    ),
    sentiment: str = Field(
        description = "Overall sentiment of the review (Positive, Negative, or Neutral)."
    ),
    rating: str = Field(
        description = "Overall rating of the review (Between 1 ~ 5)."
    )

# ==========================================
# 2️⃣ Create Structured Parser
# ==========================================
'''
This converts the blueprint into instructions the AI can understand.

> PydanticOutputParser = A tool that knows how to talk to AI about structured data
> pydantic_object=ReviewAnalysis = "Use our blueprint above"
> get_format_instructions() = Generates text telling the AI: "Return your answer in THIS exact JSON format"
'''
parser = PydanticOutputParser(pydantic_object = ReviewAnalysis)
format_instructions = parser.get_format_instructions()

# ==========================================
# 3️⃣ Define Review Input
# ==========================================
customer_review_1 = """
I recently bought the new Galaxy X smartphone, and I'm genuinely impressed!
The camera quality is stunning, and the battery lasts all day.
However, the phone feels a bit bulky and slippery.
Still, overall, it's one of the best Android phones I've used in years.
"""

customer_review_2 = """
I recently bought the new Motorola G37, and It is a good mobile!
The camera quality is good, and the battery lasts all day.
However, the design looks old.
Overall, it's one of the average Android phones I've used in years.
"""

# ==========================================
# 4️⃣ Define Prompt
# ==========================================
'''
This builds the instruction manual for the AI.

- input_variables=["review"] = The only thing that will change each time (the actual review text)
- partial_variables = Stuff that's ALWAYS the same (the format instructions)
- template = The complete instructions:
    - "Extract key information..."
    - "Follow this exact structure:" (inserts JSON format rules)
    - "Here's the review:" (inserts customer text)
'''
prompt_template = PromptTemplate(
    input_variables = ["review"],
    template = (
        "Extract the key information from the following customer review.\n"
        "Follow the structure below exactly:\n\n"
        "{format_instructions}\n\n"
        "Customer Review:\n{review}"
    ),
    partial_variables = {"format_instructions": format_instructions}
)

# ==========================================
# 5️⃣ Format Prompt
# ==========================================
formatted_prompt = prompt_template.format(review=customer_review_2)
# This combines everything into ONE final message for the AI.

# ==========================================
# 6️⃣ Send to LLM and Parse Structured Output
# ==========================================
print("🧩 Structured Output Prompting Demonstration")
print("-------------------------------------------")
print("🔹 Formatted Prompt Sent to Model:\n")
print(formatted_prompt)
print("\n🔹 Model Response:\n")

llm = get_llm()
response = llm.invoke(formatted_prompt)
raw_output = response.content

print("🔹 Raw Output:\n")
print(raw_output)
print("================================================")

print("\n🔹 Parsed JSON Output:\n")
try:
    parsed_output = parser.parse(raw_output)
    print(json.dumps(parsed_output.model_dump(), indent=2))
except Exception as e:
    print(f"[Parsing Error] {e}")



