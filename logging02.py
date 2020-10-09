import random

random_password = random.randint(10000, 99999)
print(random_password)

username = "satan98"
password = "4144835"
user_name = input("please enter your username: ")
x_password = input("Please enter x-password: ")
if user_name == username and x_password == random_password:
    print("HI")
else:
    print("check your username and x-password")
    exit()
pass_word = input("Please enter your password: ")
if user_name == username and pass_word == password and random_password == x_password:
    print("WELCOME!!!")
elif user_name != username and pass_word == password:
    print("Check your user name. ")
elif user_name == username and pass_word != password:
    print("Check your password. ")
else:
    print("Logging error")
