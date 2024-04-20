import streamlit as st

'''
Defines a table divided in three column with skills as follows:
- Technology hard skills
- Cloud skills
- Languages Spoken
'''


def define_skillset():
    # Divide the page into three columns with different width ratios
    col1, col2, col3 = st.columns([2, 2, 1])

    # Column 1: Tech Skills and Experience
    with col1:
        # Adding the skill categories as subheaders and their contents as bullet points
        st.markdown("#### 👨🏻‍💻 Languages")
        st.text("• Java 18\n• Python 3.10\n• Kotlin")

        st.markdown("#### Frameworks")
        st.text("• Spring Framework")

        st.markdown("#### Patterns & Practices")
        st.text("• Design and Enterprise Patterns\n• TDD")

        st.markdown("#### APIs & Protocols")
        st.text("• GraphQL, REST/SOAP, Web Services\n• XML, JSON Processing")

    # Column 2: Databases and Tools
    with col2:
        st.header(" ")

        st.markdown("#### ⛁ Relational Databases")
        st.text("• PostgreSQL, MySQL, Oracle")

        st.markdown("#### 🤖 Development Tools")
        st.text("• JPA, JooQ\n• Cucumber/JUnit5/Mockito\n• Agile Methodologies\n• Git/SVN/Gitlab")

        st.markdown("#### Microservices and NoSQL")
        st.text("• Microservices Architectures\n• NoSQL Databases: \n \tCassandra, DynamoDB")

    # Column 3: Cloud Experience
    with col3:
        st.markdown(" #### ☁️ Cloud Experience")
        st.text("""
        • AWS Solutions Architect
        • AWS Step Functions
        • AWS DynamoDB
        • AWS Fargate, EC2 VMs on ECS
        • AWS S3
        • Cloud and Infra Architecture
        • SNS/SQS
        • Apache Spark on AWS EMR
        • AWS OpenSearch
        • AWS RDS (Postgres DB engine)
        • AWS Lambda Serverless Functions
        • AWS CloudWatch
        • IaC: Terraform, CDK
        """)
    st.write("#")
    # Footer: Languages spoken
    st.markdown("#### Human Languages")
    st.write("🇪🇸 Spanish (Native speaker)")
    st.write("🇬🇧 English (Fluent)")
    st.write("🇩🇪 German (Basic)")

