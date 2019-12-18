try:
    num = int(input("Please input an integer: "))

    result = 8 / num

    print(result)

except ValueError:
    print("Please input correct integer!")

except Exception as result:
    print("Unknown error %s" % result)

else:
    print("Trial passed")

finally:
    print("This line will show up regardless")

print("-" * 50)