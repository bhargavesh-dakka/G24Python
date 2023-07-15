import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import mysql.connector as mysql
import smtplib, ssl

st.set_page_config(initial_sidebar_state="collapsed")



name = st.session_state.Name

reg = st.session_state.regression
classss = st.session_state.classification
unsup = st.session_state.unsuper

# st.write(classss)


def create_connection():
    mydb = mysql.connect(
        host="sql6.freemysqlhosting.net",
        user="sql6632923", #enter username here
        password="iAJBkjmxL9", #enter password here
        database="sql6632923"
    )
    return mydb

space = "_"*30

def send_mail():
        
    gmail_user = 'b9703016043b@gmail.com'
    gmail_password = 'gbdzjsfafxiuunyw'

    sent_from = gmail_user
    to = st.session_state.Email
    subject = 'Project Confirmation !'
    body = f"""
<pre><code>
Student Name           : <strong>{name}<strong> <br>
{space}<br>

<strong>Regression     : </strong><br>
{space}<br>
{reg}

{space}<br>
<strong>Classification : </strong><br>
{space}<br>
{classss}


{space}<br>
<strong>Unsupervised   : </strong><br>
{space}<br>
{unsup}

{space}<br>
</code></pre>
"""
    
    email_text = """From: Application <bhargaveshdakka@gmail.com>
To: Admin <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s


""" % (st.session_state.Email,subject,body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
#-------------------------------------------------------------------


def insert_details(name, email, reg_name, class_name, unsuper_name, feed_back):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO projects (name, email, reg_name, cla_name, uns_name, feed_back) VALUES ('{name}','{email}','{reg_name}','{class_name}','{unsuper_name}','{feed_back}');")
    connection.commit()
    connection.close()

st.markdown("""
<style>
    .css-erpbzb.edgvbvh3{
    visibility : hidden;
    }
    .css-aw8l5d.e1akgbir1{
    visibility : hidden;
    }
</style>""",unsafe_allow_html=True)

st.columns(3)[2].header(st.session_state.Name.capitalize())
st.divider()

st.write("Supervised (Regression) Project : ")
st.divider()
st.write(st.session_state.regression)
st.divider()

st.write("Supervised (Classification) Project : ")
st.divider()
st.write(st.session_state.classification)
st.divider()

st.write("Unsupervised (Clustering) Project : ")
st.divider()
st.write(st.session_state.unsuper)
st.divider()

st.divider()
st.write("Fill your feedback below !")
st.divider()
slider_value = st.slider("FeedBack ( How was your experience with the course :)",
                            min_value=1,
                            max_value=5
                            )




col1, col2 = st.columns(2)

with col1 :
    st.write("Please press the button to recieve the mail.")

with col2 :
    if st.button("Recieve Mail"):
        #inserting the values to database.
        insert_details(st.session_state.Name, st.session_state.Email, st.session_state.regression.split(":")[1], st.session_state.classification.split(":")[1], st.session_state.unsuper.split(":")[1], slider_value)
        send_mail()
        st.balloons()
        st.success("Mail sent successfully!")
