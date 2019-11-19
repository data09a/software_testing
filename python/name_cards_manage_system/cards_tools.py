import cards_input

# all cards list
card_list = []


def show_menu():

    """show menu
    """
    print("*" * 50)
    print("Welcome【Name Card Manage System】V1.0")
    print("")
    print("1. Create new name card")
    print("2. Show All cards")
    print("3. Search cards")
    print("")
    print("0. Exist")
    print("*" * 50)


def new_card():

    """create new card
    """
    print("-" * 50)
    print("Function：create new card")

    # 1. tips
    name = input("Name：")
    phone = input("Phone Number：")
    email = input("Email:：")

    # 2. save the input in to the dict
    card_dict = {"name": name,
                 "phone": phone,
                 "email": email}

    # 3. add dict into card list
    card_list.append(card_dict)

    # print(card_list)

    # 4. remind input successfully
    print("Add %s name card successfully" % card_dict["name"])


def show_all():

    print("-" * 50)
    print("Function：Show all")

    # 1. define if the card exist
    if len(card_list) == 0:
        print("Currently there is not name card in the list")

        return

    # 2. show all information
    print("Name\t\tPhone\t\tEmail")
    print("-" * 60)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s" % (
            card_dict["name"],
            card_dict["phone"],
            card_dict["email"]))

    print("-" * 60)


def search_card():

    print("-" * 50)
    print("Function：Search name card")


    find_name = input("Please input the name：")

    # for in
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("Name\t\tPhone\t\tEmail")
            print("-" * 60)

            print("%s\t\t%s\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["email"]))

            print("-" * 60)

            deal_card(card_dict)

            break
    else:
        print("We did not find %s" % find_name)


def deal_card(find_dict):

    """
    process the the dict

    """

    action_str = input("Please enter：1: modify/ 2: delete/ 0: return to previous menu")

    if action_str == "1":

        find_dict["name"] = cards_input.input_card_info(find_dict["name"],
                                                        "Please enter the name：")
        find_dict["phone"] = cards_input.input_card_info(find_dict["phone"],
                                                         "Please enter the phone number：")
        find_dict["email"] = cards_input.input_card_info(find_dict["email"],
                                                         "Please enter the email：")

        print("%s name card modify successfully！" % find_dict["name"])
    elif action_str == "2":

        card_list.remove(find_dict)

        print("Delete the name card successfully！")
