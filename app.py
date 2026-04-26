## app.py

import streamlit as st
import pandas as pd

from agents.parser_agent import parse_resume
from agents.evaluator_agent import evaluate_resume
from agents.ai_detector_agent import detect_ai
from agents.scoring_agent import scoring
from agents.decision_agent import decision
from utils.excel_report import generate_report
from utils.file_parser import parse_file

# Page config
st.set_page_config(page_title="AI Hiring Agent", layout="wide")

# UI Header
st.title("🚀 AI Hiring Agent")
st.caption("Bulk Resume Screening | AI Evaluation | Auto Decision System")

# Upload Job Description
jd_file = st.file_uploader(
    "📄 Upload Job Description",
    type=["pdf", "docx", "txt"]
)

# Upload Resumes
resume_files = st.file_uploader(
    "📂 Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# Evaluate Button
if st.button("🚀 Evaluate Candidates"):

    if not jd_file or not resume_files:
        st.warning("⚠️ Please upload both Job Description and resumes")
        st.stop()

    results = []
    progress = st.progress(0)
    status_text = st.empty()

    # Parse JD
    jd_text = parse_file(jd_file)

    # Process each resume
    for idx, resume in enumerate(resume_files):

        status_text.text(f"Processing: {resume.name}")

        try:
            # Parse Resume
            resume_text = parse_file(resume)

            # Initial State
            state = {
                "jd": jd_text,
                "resume": resume_text,
                "file_name": resume.name
            }

            # Agent Pipeline
            state = parse_resume(state)
            state = evaluate_resume(state)
            state = detect_ai(state)
            state = scoring(state)
            state = decision(state)

            # Structured Output
            results.append({
                "name": state.get("name"),
                "score": state.get("score"),
                "ai": state.get("ai"),
                "decision": state.get("decision"),
                # ✅ Newly added line: include matched skills
                "matched_skills": state.get("matched_skills"),
                "missing_skills": state.get("missing_skills")
            })

        except Exception as e:
            # Safe error handling (keeps table structure intact)
            results.append({
                "name": resume.name,
                "score": 0,
                "ai": "N/A",
                "decision": "ERROR",
                # ✅ Newly added line: placeholder for matched_skills
                "matched_skills": "ERROR",
                "missing_skills": str(e)
            })

        progress.progress((idx + 1) / len(resume_files))

    status_text.text("Finalizing results...")

    # Create DataFrame
    df = pd.DataFrame(results)

    # Sort by score
    if not df.empty and "score" in df.columns:
        df = df.sort_values(by="score", ascending=False)

    # Generate Excel Report
    report_path = generate_report(df)

    st.success("✅ Evaluation Completed Successfully")

    # Display Results
    st.subheader("📊 Evaluation Results")
    st.dataframe(df, width="stretch")

    # Download Report
    with open(report_path, "rb") as f:
        st.download_button(
            label="📥 Download Excel Report",
            data=f,
            file_name="AI_Hiring_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
