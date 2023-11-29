import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Võ Hồng Khanh")

    content = """
    Hi, I am Võ Hồng Khanh! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2017 with a 
    Master of Information System from Can Tho University in Vietnam. 
    I focus on using Python for remote sensing, I have worked with companies from various countries, such as the Center 
    for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss In-Terra, 
    and performing data mining to gain business insights with the Australian Rapid Intelligence. 
    """

    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python, Fell free to contact me!
"""

st.write(content2)

col3, col4 = st.columns([1, 1])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row["title"])

with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:
            st.header(row["title"])
