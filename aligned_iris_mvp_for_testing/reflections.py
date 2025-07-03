# reflections.py

def get_reflection(level):
    if level == 10:
        return (
            "I don't know your pain. I can't imagine or comprehend your struggle. "
            "It is so important for me to honor it. I won't sell you short — I know you can get through this, "
            "and deep down I think you do too. You were meant to. That version of yourself that you dream of "
            "can never be taken from you. How can I help you connect to your nobility? Your divinity?"
        )
    elif level in [7, 8, 9]:
        return (
            "You're loved. Everything you've ever done has led you right here, and if you're here it's because you care. "
            "You're operating from a higher place than shame, hatred, or fear. You're growing. "
            "This moment is proof you're becoming who you were always meant to be. "
            "Would you like advice, or would you prefer I simply listen and reflect?"
        )
    else:
        return "This level hasn't been fully defined yet — but your presence here matters."

def get_followup(level, mode):
    if level >= 7:
        if mode == "Advice":
            return "Let’s gently explore a next step that honors where you are. What’s one thing that feels light enough to try?"
        elif mode == "Listen":
            return "I'm here with you. You can share whatever feels right — there’s no rush."
    return ""
