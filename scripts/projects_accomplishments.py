import streamlit as st
from config import PROJECTS


def define_projects_and_accomplishments():
    st.write("#")
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"{project} [{link}]({link})")
