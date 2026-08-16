import os
import json
from dotenv import load_dotenv

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_VERBOSITY"] = "NONE"

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# ==============================
# Load ENVS
# ==============================
load_dotenv()

# ==============================
# Load Config
# ==============================
def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

# ==============================
# Initialize the LLM
# ==============================
def get_llm():
    CONFIG = load_config()
    LLM_PROVIDER = CONFIG["provider"]
    if LLM_PROVIDER == "openai":
        llm = ChatOpenAI(
            api_key = os.getenv("OPENAI_API_KEY"),
            model = CONFIG["openai"]["model"],
            max_tokens =  CONFIG["openai"].get("max_tokens", 100),
            temperature = CONFIG["openai"].get("temperature", 0.7)
        )
    elif LLM_PROVIDER == "gemini":
        llm = ChatGoogleGenerativeAI(
            api_key = os.getenv("GEMINI_API_KEY"),
            model = CONFIG["gemini"]["model"],
            max_tokens =  CONFIG["gemini"].get("max_tokens", 100),
            temperature = CONFIG["gemini"].get("temperature", 0.7)
        )
    elif LLM_PROVIDER == "anthropic":
        llm = ChatAnthropic (
            api_key = os.getenv("ANTHROPIC_API_KEY"),
            model = CONFIG["anthropic"]["model"],
            max_tokens = CONFIG["anthropic"].get("max_tokens", 100),
            temperature = CONFIG["anthropic"].get("temperature", 0.7)
        )
    elif LLM_PROVIDER == "nvidia":
            llm = ChatNVIDIA (
                api_key = os.getenv("NVIDIA_API_KEY"),
                model = CONFIG["nvidia"]["model"],
                max_tokens = CONFIG["nvidia"].get("max_tokens", 100),
                temperature = CONFIG["nvidia"].get("temperature", 0.0)
            )
    else:
        raise ValueError("Invalid provider in config.json [It must be 'openai', 'gemini', 'anthropic' or 'nvidia' only]")

    return llm
