import os

import streamlit as st
import yaml

"""
Load the work history contents file from the /resources folder, where all the work history
entries should be placed.
"""


def load_work_history():
    # Assuming the 'main.py' file is in the same directory as 'resources' folder
    yaml_file_path = os.path.join('resources', 'work_history_contents.yaml')
    with open(yaml_file_path, "r") as file:
        return yaml.safe_load(file)


'''
Defines the work history.
Could be refactored to be read from a text file and loaded with a function too.
For simplicity and quick project demonstration purposes, left at how it looks now.
'''


def define_work_history():
    work_history = load_work_history()

    st.write("#")
    st.subheader("Work History")
    st.write("---")

    for job in work_history:
        st.markdown(f"##### {job['title']}")
        st.write(f"**Time Period:** {job['period']}")
        company = job['company_url'] if 'company_url' in job else job['company']
        st.markdown(f"**Company:** [{job['company']}]({company}), Business Unit: {job['business_unit']} ")
        st.write(f"**Location**: {job['location']}")
        st.write(f"**Project**: {job['project']}")
        st.write(f"- *Technology Stack:* {job['technology_stack']}")
        st.write("#")

