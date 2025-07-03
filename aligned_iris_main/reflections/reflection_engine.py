# reflections/reflection_engine.py

import requests
import os

# Hugging Face API settings
HF_TOKEN = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/01-ai/Yi-9B-Chat"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}


def generate_reflection(prompt, style="Default", activation_level=5):
    styled_prompt = f"""
You are IrisAI — a calm, humorous, poetic, or rational assistant depending on what the user needs. 
They’ve just journaled this:

\"{prompt}\"

#This is the system prompt that I can fiddle around with in order to get a response more finely-tuned to attain the results I want
Their current activation energy is {activation_level}/10, and they’ve selected the style: {style}.

Please provide a response that is kind, precise, and encouraging — helping them lower friction and take one small step forward.
Avoid being overly therapeutic. Use humor or poetic tone only when requested.
Your reply should feel like a thoughtful friend with insight and soul.
"""
    payload = {
        "inputs": styled_prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.7,
            "top_p": 0.95
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    try:
        return response.json()[0]["generated_text"]
    except Exception as e:
        return f"[Error generating reflection: {e}]"