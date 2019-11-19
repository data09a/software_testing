def input_card_info(dict_value, tip_message):

   #input business card value

    result_str = input(tip_message)


    if len(result_str) > 0:

        return result_str

    else:

        return dict_value
