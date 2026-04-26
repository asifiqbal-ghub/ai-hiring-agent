## AI Resume Detector (ai_detector.py)

import re

def detect_ai(state):
    resume = state.get("resume", "").lower()

    # Common AI-generated buzzwords / filler phrases
    ai_phrases = [
        "results-driven", "highly motivated", "detail-oriented", "team player",
        "proven track record", "dynamic professional", "passionate about",
        "excellent communication skills", "fast learner", "hardworking individual"
    ]

    # Heuristic checks
    # 1. Count adjectives vs technical terms
    adjectives = len(re.findall(r"\b(results-driven|motivated|dynamic|passionate|excellent|hardworking)\b", resume))
    technical_terms = len(re.findall(r"\b(python|flask|fastapi|langchain|openai|azure|aws|pandas|numpy|docker|git)\b", resume))

    # 2. Check for lack of numbers/projects (AI resumes often avoid specifics)
    has_numbers = bool(re.search(r"\d+", resume))
    has_projects = "project" in resume or "experience" in resume

    # Decision logic
    if any(p in resume for p in ai_phrases):
        state["ai"] = "Yes"
    elif adjectives > technical_terms and not has_numbers and not has_projects:
        state["ai"] = "Yes"
    else:
        state["ai"] = "No"

    return state
