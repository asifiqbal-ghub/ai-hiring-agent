## parser.py

def parse_resume(state):
    # Keep candidate name
    state["name"] = state.get("file_name", "Unknown")

    # Do NOT overwrite resume text
    # Just ensure it's present
    if "resume" not in state or not state["resume"]:
        state["resume"] = ""

    return state
