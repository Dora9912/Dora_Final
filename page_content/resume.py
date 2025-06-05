import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "ChineseVersionResume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Chinese Resume",
                        data=PDFbyte,
                        file_name="Dora_Ding_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Ran Ding")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** 13779598117@163.com
    - **Phone:** (+86)13779598117
    """)

    st.header("Professional Summary")
    st.markdown("""
    I'm currently studying for my master’s in marketing at CUHK, and I graduated from Sichuan University majored in Exhibition Management. Through my internships, I've gotten real hands-on experience in digital marketing and e-commerce. Moving forward, I aspire to build a career in the e-commerce field and aim to achieve breakthroughs in this industry!
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Content Operations Intern, Purcotton Inc.**
    - *March 2025 – Present*
    - Responsible for content review, publishing, and repurposing/remixing of videos on Taobao and JD platforms, optimizing posting schedules and topic selection strategies, improving the content review SOP.
    - Responsible for organizing advertising data, analyzing video performance metrics, GMV, and ROI, conducting weekly data reviews, and setting goals for the next cycle.

    **KOL Operations Intern, Fandao**
    - *April 2024 – August 2024*
    - Identified 50+ high-potential KOLs/KOCs (audience match rate >85%), independently managed 20+ creators, and produced high-performing content with ROI>2.0 through data-driven optimization.
    - Processed and analyzed brand advertising data (500+ entries daily), optimized campaign strategies through competitor benchmarking, contributing to a 20% increase in ROI.
    - Proficient in using Douyin's Star Graph and Excel (VLOOKUP/pivot tables) for data cleansing and analysis.
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - Chinese University of HongKong
    - *Graduated: November 2025*
    - GPA: 3.7/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python,R
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)


    st.header("Languages")
    st.markdown("""
    - **English:** Business
    """)

    st.header("Interests")
    st.markdown("""
    - Bakery
    - Swimming
    - Hiking and outdoor activities
    """)

    st.markdown("---") 
