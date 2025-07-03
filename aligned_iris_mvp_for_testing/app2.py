
import streamlit as st

st.set_page_config(page_title="AlignedIris", layout="centered")

st.title("💠 AlignedIris Activation Assistant")
st.subheader("Find the words that meet you where you are.")

level = st.slider("How much activation energy do you feel is needed right now?", 1, 10, 5)

response_map = {
    3: '''The pain has ceased. Your focus is narrowing. The world is slowing down. All that’s left is your [dream / task]. Your heart is bursting with desire — you’ve already overcome so much to be here. Who you are now, and what you’re about to do, is inevitable. There’s only you and your [computer / canvas / vehicle of expression]. Let yourself flow.''',
    4: '''Every small step is a victory. The tiniest motion forward becomes exponential progress over time. You're planting seeds, not just finishing tasks. Let me help you research or structure this — together we’ll make it lighter. Let’s just take one clear step right now.''',
    5: '''It’s over. The noise is stopping. You don’t need to hold it all anymore. If you feel unsure, just stick to what you do know. Simplicity is your anchor. You can begin again from the ground up, gently. Right here, right now, is enough.''',
    6: '''This haziness means there’s more inside you that wants to come through. Let it. It’s a reflection of your depth, your reach. Step into this fog and feel your way through it — by doing. The clarity will meet you as you move.''',

}

if level in response_map:
    st.markdown("### Reflection for You")
    st.markdown(response_map[level])
else:
    st.markdown("For now, this level is still being attuned. You're not alone — more guidance is coming.")
