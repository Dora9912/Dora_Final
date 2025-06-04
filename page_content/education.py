import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **Chinese University of HongKong** | *August 2024 - November 2025*
    
    - GPA: 3.7/4.0
    - Relevant Coursework: Customer Analytics, Social Media Analytics, Marketing Research, Big Data Strategy
    
    ### Bachelor of Science in Exhibition and Economy Management
    **Sichuan University** | *September 2018 - June 2022*
    
    - GPA: 3.52/4.0
    - Relevant Coursework: Consumer Behavior, Exhibition Management, Marketing in Tourism, Project Management
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with cert2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with cert3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 
