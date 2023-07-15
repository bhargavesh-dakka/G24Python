import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os

st.set_page_config(initial_sidebar_state="collapsed")

st.session_state['unsuper'] = 0


st.markdown("""
<style>
.css-eh5xgm.e1ewe7hr3{ visibility: hidden; },
.css-cio0dv{ visibility: hidden; }
</style>
""",unsafe_allow_html=True)

st.header("Please select one project on Unsupervised Machine Learning !")
st.divider()


count = 1
path = 'UnSupervised/'


def get(details):
    name = details.split(".")[0]
    with open(path + details,"r") as f:
        desc = f.read()


    return name, desc

list_of_project_names = [f"{i+1} : {get(details)[0]} : {get(details)[1]}" for i,details in enumerate(os.listdir(path)) ]

if st.session_state.unsuper not in st.session_state:
    st.header("Select your project : ")
    st.session_state['unsuper'] = st.radio("", list_of_project_names)

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

# st.divider()
# st.write("You have Selected : (unsuper) ")
# st.write(st.session_state.unsuper)


if st.columns(3)[1].button("Display full projects information ..."):
    switch_page("Display")
