import cards_tools

while True:

    cards_tools.show_menu()

    action = input("Please choose the function：")

    print("Your choice is ：%s" % action)


    if action in ["1", "2", "3"]:

        if action == "1":
            cards_tools.new_card()

        elif action == "2":
            cards_tools.show_all()

        elif action == "3":
            cards_tools.search_card()

    elif action == "0":
        print("Welcome to the name card management system")

        break
    else:
        print("Enter wrong, please enter again：")
