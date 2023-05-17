import streamlit as st

st.header(":mailbox: Get In Touch With Us !")

contact_form = """
<form action="https://formsubmit.co/ban2kolkata@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Please give your feedback"></textarea>
     <button type="submit">Send</button>
</form> 


"""
st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("pages/css/style.css")        