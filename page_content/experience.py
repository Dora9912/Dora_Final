import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Content Operations Intern
    **Purcotton Inc.** | *March 2025 - June 2025*
    
    - Responsible for content review, publishing, and repurposing/remixing of videos on Taobao and JD platforms, optimizing posting schedules and topic selection strategies, improving the content review SOP (Standard Operating Procedure).
    - Responsible for organizing advertising data, analyzing video performance metrics, GMV, and ROI, conducting weekly data reviews, and setting goals for the next cycle.
    """)
    
    st.markdown("""
    ### KOL Operations Intern
    **Fandao Inc.** | *April 2024 - July 2024*
    
    - Identified 50+ high-potential KOLs/KOCs (audience match rate >85%), independently managed 20+ creators, and produced high-performing content with ROI>2.0 through data-driven optimization.
    - Processed and analyzed brand advertising data (500+ entries daily), optimized campaign strategies through competitor benchmarking, contributing to a 20% increase in ROI.
    - Proficient in using Douyin's Star Graph and Excel (VLOOKUP/pivot tables) for data cleansing and analysis.
    """)
    
    st.markdown("""
    ### Software Development Intern
    **InnovateTech Solutions** | *May 2020 - August 2020*
    
    - Developed and maintained web applications using Django and React
    - Collaborated with a team of developers using Agile methodologies
    - Implemented new features based on user feedback and requirements
    - Participated in code reviews and testing procedures
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 
