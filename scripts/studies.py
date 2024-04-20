import os

import streamlit as st
import yaml


# Load the work history contents file from the /resources folder

def load_studies():
    # Assuming the 'main.py' file is in the same directory as 'resources' folder
    yaml_file_path = os.path.join('resources', 'education.yaml')
    with open(yaml_file_path, "r") as file:
        return yaml.safe_load(file)


'''
Defines the studies done.
'''


def define_studies():
    studies = load_studies()

    st.write("#")
    st.subheader("Studies")
    st.write("---")

    for study in studies:
        # Use triple quotes and proper Markdown for spacing
        st.markdown(f"""
        ##### {study['degree']}
        **Time Period:** {study['period']}  
        *Institution:* {study['institution']}
        """, unsafe_allow_html=True)
