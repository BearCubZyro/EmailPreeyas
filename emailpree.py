import random
import smtplib
from email.message import EmailMessage

pushpa = False
# Generate OTP
otp = ""
for i in range(6):
    otp += str(random.randint(0, 9))

print("OTP:", otp)

# Establish connection with SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'preeyastumulu@gmail.com'
password = 'npjr xiub egwt oddx'  # Your email password, not 'from_mail'

# Login to your email account
server.login(from_mail, password)

to_mail = input("Enter your Email: ")

msg = EmailMessage()
msg['Subject'] = "OTP VERIFICATION"
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content("YOUR OTP IS: " + otp + "Do not share it with anyone else")

# Send email try and except block
server.send_message(msg)
print("Email sent")

# Close the connection

input_otp=input("Enter OTP :")
if input_otp==otp:
    print("OTP verified")
    pushpa = True
    # print(pushpa)
else :
    print("Invalid OTP ")    
    pushpa = False

if pushpa:
    print("1. Akhila project?")
    print("2. Rudra project?")
    choice = int(input("Which do you want?"))
    
    if choice == 1:
        # rudraKaCode()
        print("Rudra")
    elif choice == 2:
        # akhilaKaCode()
        print("Akhila")

server.quit()