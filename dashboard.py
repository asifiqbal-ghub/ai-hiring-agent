## Hiring Dashboard

import streamlit as st
import pandas as pd

st.title("Hiring Dashboard")

df = pd.read_excel("output/report.xlsx")

st.dataframe(df)

st.bar_chart(df["Score"])

st.metric(
    "Selected",
    len(df[df["Decision"]=="Selected"])
)