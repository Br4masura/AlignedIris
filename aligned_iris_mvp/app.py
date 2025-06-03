# app.py

import streamlit as st
from reflections import get_reflection, get_followup

st.set_page_config(page_title="AlignedIris - Soft Start", layout="centered")

st.title("🌸 AlignedIris - Soft Start System")
st.subheader("A loving prompt for gentle task activation")

# Select energy level
level = st.selectbox("💡 How hard does starting feel right now?", list(range(1, 11)), index=6)

# Show reflection
reflection = get_reflection(level)
st.write("")
st.markdown(f"**Reflection:** {reflection}")

# If in levels 7–10, offer a mode of response
if level >= 7:
    st.write("---")
    mode = st.radio("✨ What would help more right now?", ["Advice", "Listen"], horizontal=True)
    followup = get_followup(level, mode)
    st.markdown(f"**AlignedIris says:** {followup}")
