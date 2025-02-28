import streamlit as st
import sqlite3
# st.title('Welcome to my app')
# st.write('Here you can find some data about the Iris dataset')
# st.image("./img/1.jpg")
# st.checkbox('Show data')
# st.button('Click me')
# st.radio('Gender',options=['Male','Female'])
# st.selectbox("Select city",options=['New York','London','Berlin'])
def connect_db():
  conn = sqlite3.connect('mydb.db')
  #c = conn.cursor()
  return conn 

def create_table():
  conn = connect_db()
  cur = conn.cursor()
  cur.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, password TEXT, roll INT, branch TEXT)')
  conn.commit()
  conn.close()

def addRecord(data):
  conn = connect_db()
  cur = conn.cursor()
  conn.execute('INSERT INTO students (name,password,roll,branch) VALUES (?,?,?,?)',data)
  #st.success("Successfully added")
  conn.commit()
  conn.close()
  
  
def signup():
    Name = st.text_input('Name')
    password = st.text_input('Password',type='password')
    repass = st.text_input('Re-enter Password',type='password')
    Roll = st.text_input('Roll number')
    Branch = st.selectbox("Select your branch",options=['CSE','AIML','IOT'])
    if st.button('Signup '):
      if password!=repass:
        st.error("Password not matched")
      else:
        addRecord((Name,password,Roll,Branch))
signup()