import streamlit as st
import pandas


def show_item(st, row):
    name = (row["first name"] + " " + row["last name"]).title()
    st.subheader(name)
    st.markdown(f"<b>{row['role']}</b>", unsafe_allow_html=True)
    st.image("images_e/" + row["image"])


st.set_page_config(layout="wide")

st.title("The best company")

st.info("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")

st.subheader("Our Team")

col1, empty1, col2, empty2, col3 = st.columns([1, 0.1, 1, 0.1, 1])

data_e = pandas.read_csv("data_e.csv")
topics_e = pandas.read_csv("topics_e.csv")

len3 = int(len(data_e) / 3)
len3_2 = len3 * 2
with col1:
    for index, row in data_e[:len3].iterrows():
        show_item(st, row)

with col2:
    for index, row in data_e[len3:len3_2].iterrows():
        show_item(st, row)

with col3:
    for index, row in data_e[len3_2:].iterrows():
        show_item(st, row)