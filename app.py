import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("Hello, Karan here")
st.text("Hii, this is my first streamlit app.")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.video("https://www.youtube.com/watch?v=gdx7gN1UyX0&list=RDgdx7gN1UyX0&start_radio=1")

upload_file = st.file_uploader("Ponds.csv", type='csv')

if upload_file:
    df = pd.read_csv(Ponds.csv)
    st.dataframe(df)
    
st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5):\n    print(i)", language="python")


st.text_input("What is your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Cherry"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick One", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details")
    
option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")
    
    
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    
if submitted:

    st.success(f"Welcome, {username}!")
