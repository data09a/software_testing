# string define and for in

# str1 = "hello python"
# str2 = 'My name is Jack'
#
# print(str2)
# print(str1[6])
#
# for char in str2:
#
#     print(char)


##string count

# hello_str = "hello hello"
#
# # 1. length
# print(len(hello_str))
#
# # 2. count
# print(hello_str.count("llo"))
# print(hello_str.count("abc"))
#
# # 3. index number of the element
# print(hello_str.index("llo"))


# # true or false

# 1
# space_str = "      \t\n\r"
#
# print(space_str.isspace())

# 2
# num_str = "this is a string "

# print(num_str)
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isnumeric())


# # 1. true or false

# hello_str = "hello world"
#
# print(hello_str.startswith("Hello"))
#
# print(hello_str.endswith("world"))

# # 2. find index number of specific element
# print(hello_str.find("llo"))
#
# # not exist, return -1
# print(hello_str.find("abc"))

# # 3. replace elements

# print(hello_str.replace("world", "python"))
#
# print(hello_str)
# #


# poem = ["\t\n poem name",
#          "author",
#          "the first line\t\n",
#          "the second line",
#          "the third line",
#          "the fourth line"]
#
# for poem_str in poem:
#
#     print("|%s|" % poem_str.strip().center(10, "　"))



# poem_str ="poem name\t author \t the first line\t\n the second line \t\t the third line \t\t\n the fourth line"

## this is unorganized
# print(poem_str)

# # # 1. split the string one bye one
# poem_list = poem_str.split()
# print(poem_list)
# #
# # # 2. combine the string
# result = " ".join(poem_list)
# print(result)


# # function for in

# for num in [1, 2, 3]:
#
#     print(num)
#
#     if num == 2:
#         break
# else:
#
#     print("is it going to process?")
#
# print("end of loop")
# #
#

# # function

# students = [
#     {"name": "Jack"},
#     {"name": "Emily"}
# ]
#
#
# find_name = "John"
#
# for stu_dict in students:
#
#     print(stu_dict)
#
#     if stu_dict["name"] == find_name:
#
#         print("Find the name　%s" % find_name)
#
#         break
# else:
#
#     print("Sorry, did not fine name　%s" % find_name)
#
# print("End of loop")
