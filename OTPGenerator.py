import random as r
otp = ""
for i in range(6):
    temp = r.randint(0,9)
    otp += str(temp)
print("Your OTP is :",otp)
