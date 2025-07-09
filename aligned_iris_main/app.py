import streamlit as st
from pathlib import Path
import base64
from reflections.reflection_engine import generate_reflection

# Page setup
st.set_page_config(page_title="AlignedIris", layout="wide")

# --- Optional Visual Background ---
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Optional Audio Background ---
def play_audio(audio_path):
    audio_file = open(audio_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# === UI Elements ===
st.title("🌸 AlignedIris")
st.markdown("A reflective assistant to help you reconnect with clarity, balance, and gentle momentum.")

# 🌌 Visual toggle
if st.checkbox("Enable Alternative Background"):
    set_background("iris_assets/visual/impressionisticPainting.jpg")

# 🎧 Audio toggle
audio_choice = st.selectbox("Background Audio", ["None", "Tibetan Bowls", "Meditative Piano (Classical)"])
if audio_choice == "Tibetan Bowls":
    play_audio("iris_assets/audio/meditations.mp3")
elif audio_choice == "Meditative Piano (Classical)":
    play_audio("iris_assets/audio/slow.mp3")

# 🎭 Tone selector
style = st.selectbox("Choose IrisAI's Reflection Style", ["Default", "Rational", "Poetic", "Humorous"])

# ⚡ Activation Level
activation_level = st.slider("How difficult is it to begin right now? (1 = effortless, 10 = overwhelming)", 1, 10, 5)

# 📓 Journal Input
st.subheader("📓 Journal Entry")
journal = st.text_area("Write your thoughts here:", height=200)

# 💬 Reflection Trigger
if journal and st.button("💬 Reflect with IrisAI"):
    with st.spinner("IrisAI is gently thinking..."):
        reflection = generate_reflection(journal, style, activation_level)

    st.subheader("🌼 IrisAI Reflects")
    st.info(reflection)