"""
Welcome to Kodi's Cafe
Please sign in!

Insert your username : kodi
Insert your email : kodi@botica.com
Insert your password : 12345

Welcome to the System! You are logged in!
OR
Invalid Credentials!
"""

print("Welcome to Kodi's Cafe, Please sign in!")

username = input("Insert your username: ")
email = input("Insert your email: ")
password = input("Insert your password: ")

if username == "kodi" and email == "kodi@botica.com" and password == "12345":
    print("Welcome to the System! You are logged in!")
else:
    print("Invalid Credentials!")