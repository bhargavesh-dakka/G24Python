import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
import mysql.connector as mysql

st.set_page_config(initial_sidebar_state="collapsed")

def create_connection():
    mydb = mysql.connect(
        host="sql6.freemysqlhosting.net",
        user="sql6632923", #enter username here
        password="iAJBkjmxL9", #enter password here
        database="sql6632923"
    )
    return mydb

def fetch_classification():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT cla_name FROM projects;")
    reg_list = [i[0] for i in cursor.fetchall()]
    connection.close()
    return list(reg_list)

already_selected = fetch_classification()

st.session_state['classification'] = 0


st.markdown("""
<style>
.css-eh5xgm.e1ewe7hr3{ visibility: hidden; },
.css-cio0dv{ visibility: hidden; }
</style>
""",unsafe_allow_html=True)

st.header("Please select one project on Classification !")
st.divider()


count = 1
path = 'Classification/'


def get(details):
    name = details.split(".")[0]
    if name not in already_selected:
        with open(path + details,"r") as f:
            desc = f.read()
    return name, desc

list_of_project_names = [f"{i+1} : {get(details)[0]} : {get(details)[1]}" for i,details in enumerate(os.listdir(path)) ]

if st.session_state.classification not in st.session_state:
    st.header("Select your project : ")
    st.session_state['classification'] = st.radio("", list_of_project_names)

# st.session_state.classification = st.session_state.classification.split(":")[1]
# st.divider()
# st.write("Your name : ")
# st.write(st.session_state.Name.capitalize())

# st.divider()
# st.write("You have Selected : (Regression) ")
# st.write(st.session_state.regression)

# st.divider()
# st.write("You have Selected : (classification) ")
# st.write(st.session_state.classification)


if st.columns(5)[2].button("Continue ..."):
    if st.session_state.classification.split(":")[1] in already_selected:
        st.error("This project has already been selected! Please select another.")
    else:
        switch_page("Clustering")

