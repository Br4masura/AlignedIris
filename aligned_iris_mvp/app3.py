import streamlit as st
import os
from datetime import datetime
import random

# --- Constants ---
MEDIA_DIR = "media"
ACTIVATION_LEVELS = list(range(1, 11))

# --- Prompt Logic Engine (basic heuristic) ---
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

# Display background visual
visuals = [f for f in os.listdir(visual_path) if f.endswith((".jpg", ".png", ".mp4"))] if os.path.exists(visual_path) else []
if visuals:
    st.image(os.path.join(visual_path, visuals[0]), use_column_width=True)

# Display audio player
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
