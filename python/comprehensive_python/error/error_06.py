def input_password():
    pwd = input("Please input password: ")

    if len(pwd) >= 8:
        return pwd
    # if < 8  show error
    print("Error")
    ex = Exception("Password length is too short")

    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)
