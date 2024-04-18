from pathlib import Path
from PIL import Image
import streamlit as st

# Import configuration settings
from config import *
from tools.assets_manager import AssetManager

# Set page configuration first
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

assets_manager = AssetManager()
css_file_contents = assets_manager.get_css()
resume_file_contents = assets_manager.get_resume()
profile_pic_contents = assets_manager.get_profile_pic()

st.title("Hello There!")

# Load CSS, PDF and PROFILE asset's contents
st.markdown("<style>{}</style>".format(css_file_contents), unsafe_allow_html=True)
profile_picture = Image.open(profile_pic_contents)

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_picture, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resumè",
        data = resume_file_contents,
        file_name = assets_manager.get_resume_filename(),
        mime = "application/octet-stream"
    )
    st.write("📧", EMAIL)
