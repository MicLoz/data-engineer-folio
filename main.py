import streamlit as st
from colour_picker import colour_picker_section, return_custom_styling

st.title("Michael Lozynsky")
st.title("Data Engineering Portfolio")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a Project", ["Home", "ETL Pipeline", "Data Warehouse", "Real-Time Processing"])
st.sidebar.title("Customisation")
with st.sidebar.expander("Customise Theme Colours"):
    theme_colours = colour_picker_section()

custom_style = return_custom_styling(theme_colours)
st.markdown(custom_style, unsafe_allow_html=True)

if option == "Home":
    st.header("About Me")
    st.write("""
             I am a skilled data professional with a strong background in quality assurance and data engineering.
             \nMy most recent experience involved testing financial reports
             for a large job management software company serving over 2,400 customers and maintaining 1,000+ 
             reports. 
             \nThis role honed my expertise in writing complex SQL queries, testing stored procedures, 
             and performing comprehensive UI testing.
             \nI also contributed to development efforts, 
             including building data marts with DBT, creating data connectors to work with Snowflake, and creating detailed reports. 
             \nAdditionally, I automated testing processes using C# and Selenium to ensure the accuracy and reliability
             of critical reports. 
             \nPreviously, I was promoted to QA Analyst from a second-line support analyst position 
             due to my ability to recreate and diagnose difficult-to-track issues, 
             demonstrating my analytical skills and problem-solving capabilities.
             \nI have excellent SQL skills and have recently developed proficiency in Python 
             through dedicated training. 
             This complements my experience in automation, data modeling, and testing workflows. 
             \nEarlier in my career, I worked in online retail, where I gained valuable experience in copywriting 
             and e-commerce operations by creating optimized listings on platforms like Amazon and eBay.
             \nWith a passion for data engineering, I am eager to leverage my diverse technical background 
             to build robust data pipelines and solutions that drive business insights and operational efficiency.
             """
             )

elif option == "ETL Pipeline":
    st.header("ETL Pipeline Project")
    st.write("Description of the project.")
    st.code("""
    # Example ETL pipeline code
    import pandas as pd
    data = pd.read_csv('data.csv')
    cleaned_data = data.dropna()
    cleaned_data.to_csv('cleaned_data.csv', index=False)
    """)

elif option == "Data Warehouse":
    st.header("Data Warehouse Project")
    st.write("Details about the data warehouse you built.")

elif option == "Real-Time Processing":
    st.header("Real-Time Processing Project")
    st.write("Description of real-time processing implementation.")
