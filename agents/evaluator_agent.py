## evaluator.py

def evaluate_resume(state):
    jd = state.get("jd", "").lower()
    resume = state.get("resume", "").lower()

    # Define required skills explicitly or extract dynamically from JD
    required_skills = [
        "python", "fastapi", "flask", "langchain", "llm",
        "azure", "aws", "openai", "rest api", "pandas", "numpy", "git"
    ]

    matched = [skill for skill in required_skills if skill in resume]
    missing = [skill for skill in required_skills if skill not in resume]

    score = (len(matched) / len(required_skills)) * 100 if required_skills else 0

    state["score"] = round(score, 2)
    state["matched_skills"] = ", ".join(matched) if matched else "None"
    state["missing_skills"] = ", ".join(missing) if missing else "None"

    return state

