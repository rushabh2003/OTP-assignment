# -*- coding: utf-8 -*-
"""RushabhOtpGenerator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JGnbGj8bnvFCjEjMjrpXkDPwd8Q9V5hb
"""

# OTP to mail

import smtplib
import random

sender = "aradwadrushabh@gmail.com"
password = "hwjpsgjqncvzfcxf"
receiver = input("Enter your email id to generate otp : ")
body = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes."

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender, password)

server.sendmail(sender, receiver, body)

print("Mail sent")