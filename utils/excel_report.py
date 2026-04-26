import os

def generate_report(df):

    os.makedirs("output", exist_ok=True)

    file_path = "output/hiring_report.xlsx"

    # Select only required columns
    df = df[[
        "name",
        "score",
        "ai",
        "decision",
        "missing_skills"
    ]]

    df.columns = ["Name", "Score", "AI", "Decision", "Missing Skills"]

    df.to_excel(file_path, index=False)

    return file_path