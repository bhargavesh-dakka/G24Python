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

def fetch_regression():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT reg_name FROM projects;")
    reg_list = [i[0] for i in cursor.fetchall()]
    connection.close()
    return list(reg_list)

already_selected = fetch_regression()
# st.write(already_selected)

st.session_state['regression'] = 0


st.markdown("""
<style>
.css-eh5xgm.e1ewe7hr3{ visibility: hidden; },
.css-cio0dv{ visibility: hidden; }
</style>
""",unsafe_allow_html=True)

st.header("Please select one project on Regression !")
st.divider()


count = 1
path = 'Regression/'


def get(details):
    name = details.split(".")[0]
    if name not in already_selected:
        with open(path + details,"r") as f:
            desc = f.read()
    return name, desc

list_of_project_names = [f"{i+1} : {get(details)[0]} : {get(details)[1]}" for i,details in enumerate(os.listdir(path)) if get(details)[0] not in already_selected ]


if st.session_state.regression not in st.session_state:
    st.header("Select your project : ")
    st.session_state['regression'] = st.radio("", list_of_project_names)

# st.session_state.regression = st.session_state.regression_project.split(":")[1]
# st.divider()
# st.write("Your name : ")
# st.write(st.session_state.Name.capitalize())

# st.divider()
# st.write("You have Selected : (Regresion) ")
# st.write(st.session_state.regression)



if st.columns(5)[2].button("Continue ..."):
    if st.session_state.regression.split(":")[1] in already_selected:
        st.error("This project has already been selected! Please select another.")
    else:
        switch_page("Classification")