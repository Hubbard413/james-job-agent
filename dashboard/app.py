
import streamlit as st
import pandas as pd

st.title("James Job Agent")

jobs = pd.read_csv("jobs.csv")

st.metric("Jobs Found", len(jobs))

st.dataframe(jobs)
