username = "satan98"
password = "12345"
user_name = input("please enter your username? ")
pass_word = input("Please enter your password? ")
if user_name == username and pass_word == password:
    print("WELCOME!!!")
elif user_name != username and pass_word == password:
    print("Check your user name. ")
elif user_name == username and pass_word != password:
    print("Check your password. ")
else:
    print("Logging error")
