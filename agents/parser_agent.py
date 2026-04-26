## parser.py

def parse_resume(state):

    state["name"] = state.get("file_name", "Unknown")

    return state