import time
import requests
import config
import re
    

while True:
    MOBILE_NUMBER = int(input("Enter Mobile Number: "))
    global config
    url = "https://88panel.com/forgot_otp/winbuzz.com"
    data = {"mobile": MOBILE_NUMBER, "_token": config.TOKEN}
    response = requests.post(url, data=data)
    if re.search(r"OTP sent success !",response.text):
        print()
        print("Succes: OTP sent Successfully Dude......!!!")
        break
    elif re.search(r"Mobile number not registered !", response.text):
        print("Failure")
    else:
        print("Error Occurred...!!!:", response.status_code,response.text)
