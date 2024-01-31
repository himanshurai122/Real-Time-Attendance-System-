import streamlit as st
st.set_page_config(page_title='Attendance system',layout='wide')
st.header('Attendance system using face recognition')

with st.spinner("Loading models and connecting to redis db.."):
    import face_rec

st.success('Model loaded successfully')
st.success('Redis db connected successfullyy')
