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
    ### Marketing Intern
    **Ecolab** | *October 2023 - March 2024*
    
    - Independently designed and developed a new warehouse gift management system for the business division, covering the gift receiving module to achieve automatic and precise management and control of the warehouse.
    - In the global sales assault activity, I was responsible for the early activity planning, the middle process control, and the late arrangement of background sales data and the production of promotional videos. The sales volume reached 1millionUSD in one week.
    - Independently interviewed the relevant personnel of the skills competition, produced the bilingual magazine in Chinese and English after the competition, published it to the global head office, and the reading volume reached 5000+; 100% responsible for the International Women's Day interview activity, design and produce posters, which have been read more than 3000 times after publication.
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Data Processing:** Pandas, NumPy, PySpark
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
