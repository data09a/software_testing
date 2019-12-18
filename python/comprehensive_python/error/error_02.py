try:
    num = int(input("Please input an integer: "))

    result = 8 / num

    print(result)

except ZeroDivisionError:
    print("Divide 0 error")

except ValueError:
    print("Please input correct integer!")