import streamlit as st
import os
from datetime import datetime
import random
from transformers import pipeline

# --- Constants ---
MEDIA_DIR = "media"
ACTIVATION_LEVELS = list(range(1, 11))

# --- AI Reflection Engine ---
reflector = pipeline("text-generation", model="gpt2")  # Can be replaced with more powerful model

def generate_iris_response(journal_text):
    intro = "This journal entry is from someone reflecting deeply. Respond with kindness, insight, and encouragement."
    prompt = f"{intro}\n\nEntry: {journal_text}\n\nIrisAI:"
    result = reflector(prompt, max_length=150, do_sample=True, temperature=0.8)[0]['generated_text']
    response = result.split("IrisAI:")[-1].strip()
    return response

# --- Prompt Logic Engine ---
def generate_prompt(level):
    growth_prompts = [
        "What's one small step toward your growth today?",
        "What did you learn recently that surprised you?",
        "What part of yourself are you beginning to embrace?"
    ]
    balance_prompts = [
        "How can you simplify something today?",
        "What emotion is most present right now?",
        "What's something you can release control over today?"
    ]
    flow_prompts = [
        "What activity makes you lose track of time?",
        "How does your body feel about starting this task?",
        "What's the smallest action that could begin the flow?"
    ]

    if level <= 3:
        return random.choice(flow_prompts)
    elif level <= 6:
        return random.choice(balance_prompts)
    else:
        return random.choice(growth_prompts)

# --- App UI ---
st.set_page_config(page_title="AlignedIris Journal", layout="wide")
st.title("🌸 AlignedIris - Journaling for Activation")

level = st.slider("Select your current activation level:", 1, 10, 5)

# Load background audio/visual if available
audio_path = os.path.join(MEDIA_DIR, f"level_{level}", "audio")
visual_path = os.path.join(MEDIA_DIR, f"level_{level}", "visual")

visuals = [f for f in os.listdir(visual_path) if f.endswith((".jpg", ".png", ".mp4"))] if os.path.exists(visual_path) else []
if visuals:
    st.image(os.path.join(visual_path, visuals[0]), use_column_width=True)

audios = [f for f in os.listdir(audio_path) if f.endswith(".mp3")] if os.path.exists(audio_path) else []
if audios:
    audio_file_path = os.path.join(audio_path, audios[0])
    audio_bytes = open(audio_file_path, 'rb').read()
    st.audio(audio_bytes, format='audio/mp3')

# Prompt + Journal
st.subheader("🪞 Reflective Prompt")
prompt = generate_prompt(level)
st.markdown(f"> *{prompt}*")

st.subheader("📝 Journal Entry")
journal_text = st.text_area("Write what's on your heart or mind today:", height=200)

if st.button("Save Entry"):
    if journal_text.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"entry_{timestamp}.txt"
        save_path = os.path.join("journals", filename)
        os.makedirs("journals", exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(f"Activation Level: {level}\nPrompt: {prompt}\n\n{journal_text}")
        st.success("Your reflection has been saved 💾")
    else:
        st.warning("Please write something before saving.")

# IrisAI Reflection
if journal_text.strip():
    if st.button("🧠 Reflect with IrisAI"):
        with st.spinner("IrisAI is thinking deeply with you..."):
            iris_response = generate_iris_response(journal_text)
        st.markdown("---")
        st.subheader("💡 IrisAI Reflects:")
        st.markdown(f"> {iris_response}")
