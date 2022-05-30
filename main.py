import streamlit as st
import time
import random
import streamlit.components.v1 as components


st.set_page_config(
     page_title="Privacy-Policy",
     page_icon="🏎️",
     layout="wide",
     initial_sidebar_state="expanded",

     
 )
 
def main():
    st.markdown("<h1 style='text-align: center; color:red;'>Privacy Policy</h1>", unsafe_allow_html=True)
    st.markdown("PET NET is our application which help you to find the diseases affected by your pets." 
    " It is hard to find the diseases affected by pets, we don't even know what is the cause and it's affect towards humans."
    "Privacy Policy -- provides the fast way in produce results.")
    ("When you use these services, you'll share some information with us. So we want to be upfront about the information we collect, how we use it "
    "and the controls we give you to access, update your information.")
    ("That's why we've written this Privacy Policy. And it's why we've tried to write it in a way that's easy to understand for all our users and blissfully free of the legalese that often clouds these documents.")
    st.markdown("<p style='font-family:Courier; color:Orange; font-size: 35px;'>Information we collect</p>", unsafe_allow_html=True)
    "→  There are 2 basic categories of information we collect:"
    "•  Information you provide"
    "•  Information we get when you use our services."
    st.markdown("<p style='font-family:Courier; color:Orange; font-size: 25px;'>Information you provide</p>", unsafe_allow_html=True)
    ("When you interact with our services, we collect infromation that you provide to us. For example, many of our services require you to set up an account,"
    " so we may need to collect a few important details about you, such as your name, username, password, email address and phone number."
    " We may also ask you to provide us with some additional information that will be publicy visible on our services, such as a profile picture.")
    st.markdown("<p style='font-family:Courier; color:Orange; font-size: 25px;'>Information we get when you use our services</p>", unsafe_allow_html=True)
    ("When you use our services, we collect such as images of animals affected by diseases, to find the disease name.")



if __name__ == "__main__":
    main()
    