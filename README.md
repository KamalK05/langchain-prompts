# 🎯 LangChain Prompt Engineering

A comprehensive Python repository demonstrating modern **Prompt Engineering techniques** in **LangChain**—ranging from basic string templates and role-based chat prompts to structured outputs, few-shot prompting, and external YAML template management.

---

## 🔌 Supported Providers & Architecture (`llm_provider.py`)

The repository features a unified provider factory `llm_provider.py` that handles seamless switching between leading LLM models. Selection is easily controlled via `config.json`.

| Icon | Provider | Integration Class | Required Environment Variable | Default Model (`config.json`) |
| :---: | :--- | :--- | :--- | :--- |
| <img src="https://simpleicons.org/icons/nvidia.svg" width="20" height="20"/> | **NVIDIA NIM** | `ChatNVIDIA` | `NVIDIA_API_KEY` | `nvidia/nemotron-mini-4b-instruct` |
| <img src="https://www.svgrepo.com/show/306500/openai.svg" width="20" height="20"/> | **OpenAI** | `ChatOpenAI` | `OPENAI_API_KEY` | `gpt-4o-mini` |
| <img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-gemini-icon.svg" width="20" height="20"/> | **Google Gemini** | `ChatGoogleGenerativeAI` | `GEMINI_API_KEY` | `gemini-1.5-flash` |
| <img src="https://simpleicons.org/icons/anthropic.svg" width="20" height="20"/> | **Anthropic** | `ChatAnthropic` | `ANTHROPIC_API_KEY` | `claude-3-5-sonnet-20240620` |

---

## 🤖 Core Prompting Modules

| Icon | Prompting Technique | Python Script | Key Concept Demonstrated |
| :---: | :--- | :--- | :--- |
| 📝 | **Basic Prompt Template** | `01_basic_prompt_template.py` | Simple key-value string formatting with `PromptTemplate` |
| 💬 | **Chat Prompt Template** | `02_chat_prompt_template.py` | Structuring multi-role conversations (`SystemMessage`, `HumanMessage`) |
| 💡 | **Few-Shot Prompting** | `03_few_shot_prompting.py` | Contextual learning using example sets via `FewShotPromptTemplate` |
| 🧠 | **Chain-of-Thought (CoT)** | `04_chain_of_thought_prompting.py` | Step-by-step reasoning prompts for complex problem solving |
| 🎭 | **Role-Based Prompting** | `05_role_based_prompting.py` | Defining clear agent personas, boundaries, and domain rules |
| 📊 | **Structured Output** | `06_structred_output_prompting.py` | Enforcing validated Pydantic models & JSON schemas |
| 🎯 | **Few-Shot Structured** | `07_few_shot_structured_prompting.py` | Combining exemplar learning with strict structured schemas |
| 💾 | **Save Prompt (YAML)** | `08a_create_and_save_prompt_yaml.py` | Serializing dynamic prompt templates to YAML format |
| 📂 | **Load Prompt (YAML)** | `08b_load_and_run_prompt_yaml.py` | Dynamic loading and execution of pre-configured YAML prompts |

---

## 🌟 Key Features

* **🔌 Unified LLM Factory (`llm_provider.py`)**: Effortlessly switch execution backends across OpenAI, Gemini, Anthropic, and NVIDIA NIM.
* **⚙️ JSON Configuration (`config.json`)**: Fine-tune provider settings, default models, temperature, and token thresholds centrally.
* **📐 Structured Pydantic Integration**: Enforce strict JSON output schemas for downstream data pipelines.
* **📦 YAML Serialization**: Decouple prompt logic from Python code by persisting and loading prompts as standard `.yaml` templates.
* **🚀 Zero-Dependency overhead**: Modern, clean Python scripts designed for rapid prototyping and learning.

---

## 📁 Project Structure

```text
langchain-prompts/
├── 📄 01_basic_prompt_template.py          # Basic string variable prompt templates
├── 📄 02_chat_prompt_template.py           # Multi-role message templates (System/Human)
├── 📄 03_few_shot_prompting.py             # Exemplar-based few-shot prompt construction
├── 📄 04_chain_of_thought_prompting.py     # Reasoning & step-by-step thinking prompts
├── 📄 05_role_based_prompting.py           # Persona definition & task role-playing
├── 📄 06_structred_output_prompting.py     # Pydantic schema structured output parsing
├── 📄 07_few_shot_structured_prompting.py  # Structured outputs guided by few-shot examples
├── 📄 08a_create_and_save_prompt_yaml.py   # Serializing prompt templates to disk (YAML)
├── 📄 08b_load_and_run_prompt_yaml.py      # Executing stored YAML prompt templates
├── 🔌 llm_provider.py                     # Universal provider factory class
├── ⚙️ config.json                         # Global configuration file for models & parameters
├── 📋 requirements.txt                    # Project dependencies
├── 🔑 .env                                # API keys and secret management
└── 📘 README.md                           # Documentation
```

---

## 🚀 Quick Start Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/langchain-prompts.git
cd langchain-prompts
```

### 2️⃣ Create & Activate Virtual Environment

* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment & Provider Configuration

1. **Configure API Keys**: Add your API key(s) to `.env` in the root folder:
   ```env
   NVIDIA_API_KEY="nvapi-..."
   OPENAI_API_KEY="sk-..."
   GEMINI_API_KEY="AIzaSy..."
   ANTHROPIC_API_KEY="sk-ant-..."
   ```

2. **Select Provider & Model (`config.json`)**:
   Set `"provider"` to `"nvidia"`, `"openai"`, `"gemini"`, or `"anthropic"`:
   ```json
   {
     "provider": "openai",
     "nvidia": {
       "model": "nvidia/nemotron-mini-4b-instruct",
       "max_tokens": 100,
       "temperature": 0.0
     },
     "openai": {
       "model": "gpt-4o-mini",
       "max_tokens": 100,
       "temperature": 0.7
     },
     "gemini": {
       "model": "gemini-1.5-flash",
       "max_tokens": 100,
       "temperature": 0.7
     },
     "anthropic": {
       "model": "claude-3-5-sonnet-20240620",
       "max_tokens": 100,
       "temperature": 0.7
     }
   }
   ```

---

## ▶️ Execution Commands

Run any prompt engineering script directly using Python:

### 1. Basic String Prompt Template
Demonstrates variable substitution inside standard prompt templates.
```bash
python 01_basic_prompt_template.py
```
### 2. Multi-Role Chat Prompt Template
Demonstrates multi-turn conversation formatting using SystemMessage and HumanMessage.
```bash
python 02_chat_prompt_template.py
```

### 3. Few-Shot Exemplar Prompting
Demonstrates how to pass formatted example input-output pairs to guide model completions.
```bash
python 03_few_shot_prompting.py
```
### 4. Chain-of-Thought (CoT) Prompting
Demonstrates step-by-step reasoning prompts to solve logic and complex reasoning problems.
```bash
python 04_chain_of_thought_prompting.py
```
### 5. Role-Based Prompting
Demonstrates persona definition, behavioral constraints, and domain-specific roles.
```bash
python 05_role_based_prompting.py
```

### 6. Structured Output Prompting
Demonstrates parsing and validating responses into strongly typed Pydantic models.
```bash
python 06_structred_output_prompting.py
```

### 7. Few-Shot Structured Output Prompting
Demonstrates combining structured schema validation with exemplar few-shot learning.
```bash
python 07_few_shot_structured_prompting.py
```
### 8. Save Prompt Template to YAML
Serializes dynamic LangChain prompt templates into reusable .yaml files.
```bash
python 08a_create_and_save_prompt_yaml.py
```
### 9. Load & Run Prompt Template from YAML
Loads a pre-configured prompt template from a .yaml file and executes it with an LLM.
```bash
python 08b_load_and_run_prompt_yaml.py
```

