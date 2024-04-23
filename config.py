"""
File holds configuration values for CV's contents that are not lengthy
For lengthy contents, such as work history and so on, see resources files and separate
python script to load them.
"""

# --- GENERAL SETTINGS ---
NAME = "Juan Marcos Bruno"
PAGE_TITLE = f"Digital CV | {NAME}"
PAGE_ICON = ":wave:"
DESCRIPTION = """
Cloud Architect. Lead Software Developer. Senior Software Engineer. Technology enthusiast
"""
EMAIL = "juan.marcos.bruno@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "uncomment_add_youtube_page_here",
    "LinkedIn": "https://www.linkedin.com/in/juanmarcosbruno/",
    "GitHub (Python)": "https://github.com/jmb-python-developer",
    # "Twitter": "uncomment_add_twitter_profile_here",
}
PROJECTS = {
    "Creator of the course **'Master Big Data with Apache Spark and Java' on the Educative e-learning platform:**": "https://www.educative.io/courses/mastering-big-data-apache-spark-java-api",
}

# If others are added make sure to include the dash always for proper li and formatting by streamlit
EXPERIENCE_QUALIFICATIONS = [
    """
- Senior Software Engineer in the development and maintenance of an ecosystem of microservices for Payroll Calculations
BU in Personio (www.personio.de) , also recently involved in Cloud design, architecture and implementation
of social networks’ features for the Poppulo Harmony platform (www.poppulo.com ).
    """,
    """
- Formerly the Lead Software Developer for the Batch Solutions Team in Equifax; design, architecture and implementation
of a fully Cloud-Based Big Data application.
    """,
    """
- Worked previously on Cloud Microservices architectures, utilizing Java (functional and non-functional) and Spring
framework's family of modules. Further back in my career have also participated in the development of Post Trade
software, J2EE compliant JAVA applications, as well as in the development of Java and GRAILS RESTful APIs.
    """
]
