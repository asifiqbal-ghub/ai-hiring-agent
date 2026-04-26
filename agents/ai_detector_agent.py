## AI Resume Detector (ai_detector.py)

def detect_ai(state):

    resume = state.get("resume", "").lower()

    ai_phrases = [
        "results-driven",
        "highly motivated",
        "detail-oriented",
        "team player"
    ]

    if any(p in resume for p in ai_phrases):
        state["ai"] = "Yes"
    else:
        state["ai"] = "No"

    return state