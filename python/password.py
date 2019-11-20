def input_password():

    pwd = input("Please enter the password：")

    if len(pwd) >= 8:
        return pwd

    print("The input can not be accepted")

    ex = Exception("The password length is minimum 8 digits")

    raise ex


# password input reminding:
try:
    print(input_password())
except Exception as result:
    print(result)
