import os

import streamlit as st
import yaml


def load_skills():
    # Assuming the 'main.py' file is in the same directory as 'resources' folder
    yaml_file_path = os.path.join('resources', 'skills.yaml')
    with open(yaml_file_path, 'r') as file:
        return yaml.safe_load(file)


def display_skills(skills):
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        st.markdown("#### 👨🏻‍💻 Coding")
        for category, items in skills['tech_skills'].items():
            st.markdown(f"##### {category.title().replace('_', ' ')}")
            for item in items:
                st.text(f"• {item}")

    with col2:
        st.markdown("#### ⛁ Cloud Skills")
        for item in skills['cloud_skills']:
            st.text(f"• {item}")

    with col3:
        st.markdown("#### 🗣️ Languages Spoken")
        for item in skills['languages_spoken']:
            st.text(f"• {item}")


def define_skillset():
    st.write("#")
    st.subheader("Tech Skills")
    skills = load_skills()
    display_skills(skills)
