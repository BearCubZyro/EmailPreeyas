import os
import random
import smtplib
from email.message import EmailMessage
import streamlit as st

# Environment variables
EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

def generate_otp():
    """Generate a 6-digit OTP"""
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    return otp

def send_email(to_email, otp):
    """Send an email with the OTP"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    msg = EmailMessage()
    msg['Subject'] = "OTP VERIFICATION"
    msg['From'] = EMAIL_USERNAME
    msg['To'] = to_email
    msg.set_content("YOUR OTP IS: " + otp + "Do not share it with anyone else")
    try:
        server.send_message(msg)
        print("Email sent")
    except Exception as e:
        print("Error sending email:", e)
    finally:
        server.quit()

def verify_otp(otp, input_otp):
    """Verify the OTP"""
    if input_otp == otp:
        return True
    else:
        return False

def main():
    st.title("OTP Verification")
    to_email = st.text_input("Enter your Email:")
    otp = generate_otp()
    st.write("OTP:", otp)
    send_email(to_email, otp)
    input_otp = st.text_input("Enter OTP:")
    if verify_otp(otp, input_otp):
        st.write("OTP verified")
        pushpa = True
    else:
        st.write("Invalid OTP")
        pushpa = False
    
    if pushpa:
        st.write("1. Akhila project?")
        st.write("2. Rudra project?")
        choice = st.selectbox("Which do you want?", [1, 2])
        if choice == 1:
            st.write("Rudra")
        elif choice == 2:
            st.write("Akhila")

if __name__ == "__main__":
    main()
