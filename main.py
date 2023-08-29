import streamlit as st
from streamlit_extras import switch_page_button
import mysql.connector as mysql

st.set_page_config(initial_sidebar_state="collapsed")

def create_connection():
    mydb = mysql.connect(
        host="sql12.freemysqlhosting.net",
        user="sql12643104", #enter username here
        password="DyxC7PnUFi", #enter password here
        database="sql12643104"
    )
    return mydb

def fetch_mail():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM projects;")
    mail_list = [i[0] for i in cursor.fetchall()]
    connection.close()
    return list(mail_list)


with open(r"style.css") as f:
    st.markdown(f"<script>{f.read()}</script>",unsafe_allow_html=True)


st.markdown("<style>.css-aw8l5d.e1akgbir1, .eyeqlp51.css-fblp2.ex0cdmw0 { visibility : hidden}</style>",unsafe_allow_html=True)

st.header("Ola! 👋")
st.divider()

st.markdown("_Please select the projects from Supervised (Regression, Classification), Unsupervised (Clustering)_")


st.session_state["Name"] = st.text_input("Enter your name : ")
st.session_state["Email"] = st.text_input("Enter your Email : ")


if st.columns(5)[2].button("Continue ..."):
    if st.session_state.Name and st.session_state.Email and "@" in st.session_state.Email : 
        if st.session_state.Email not in fetch_mail(): 
            switch_page_button.switch_page("Regression")
        else: 
            st.error("User has already taken the project")
    else:    
        st.error("NOTE : please enter valid details to get Continue button!")


