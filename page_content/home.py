import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Ran Ding</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        Unit H 7/H Tower 7 The Regent, Tai Po, HK<br>
        <a href="mailto:13779598117@163.com">13779598117@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image2.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        Hi !  I'm Ding Ran. I'm currently studying for my Master's in Marketing at CUHK, and I graduated from Sichuan University majored in Exhibition Management.
        
        Through my internships, I've gotten real hands-on experience in digital marketing and e-commerce.

        Moving forward, I aspire to build a career in the e-commerce field and aim to achieve breakthroughs in this industry!  
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Work Skill: Word, Powerpoint, Excel, Pr, Ps
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
