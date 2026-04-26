## evaluator.py

def evaluate_resume(state):

    jd = state.get("jd", "").lower()
    resume = state.get("resume", "").lower()

    jd_words = set(jd.split())
    resume_words = set(resume.split())

    matched = jd_words & resume_words
    missing = jd_words - resume_words

    score = (len(matched) / len(jd_words)) * 100 if jd_words else 0

    state["score"] = round(score, 2)
    state["missing_skills"] = ", ".join(list(missing)[:5])

    return state