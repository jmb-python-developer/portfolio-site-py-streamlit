from PIL import Image

# Import configuration settings
from config import *
from helper_classes.assets_manager import AssetManager
from scripts.skills import *
from scripts.work_history import *
from scripts.projects_accomplishments import define_projects_and_accomplishments
from scripts.studies import define_studies

# Set page configuration first
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

assets_manager = AssetManager()
css_file_contents = assets_manager.get_css()
resume_file_contents = assets_manager.get_resume()
profile_pic_contents = assets_manager.get_profile_pic()

st.title(PAGE_TITLE)

# Load CSS, PDF and PROFILE asset's contents
st.markdown("<style>{}</style>".format(css_file_contents), unsafe_allow_html=True)
profile_picture = Image.open(profile_pic_contents)

# Create two columns for image and profile summary
col1, col2 = st.columns([1, 1])

with col1:
    st.image(profile_picture, width=230)

# Main Information Section
with col2:
    st.markdown(f" ### AWS Certified Cloud Architect")
    st.write(DESCRIPTION)
    st.download_button(
        label="Download CV PDF",
        data=resume_file_contents,
        file_name=assets_manager.get_resume_filename(),
        mime="application/octet-stream"
    )
    st.write(" 📧 ", EMAIL)

# Social Networks Links Section
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience and Qualifications Section
st.write("#")
st.subheader("Summary of Experience and Qualifications")
st.write(f"\n".join(EXPERIENCE_QUALIFICATIONS))

# Skills Section
define_skillset()
# Work History Section
define_work_history()
# Far in the past - other experience section
define_other_past_experience()
# Projects and Accomplishments
define_projects_and_accomplishments()
# Studies
define_studies()

