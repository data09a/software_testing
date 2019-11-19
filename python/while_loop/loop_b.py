#requirements: print multiplication table

#STEP 1
# row = 1
#
# while row <= 9:
#
#     col = 1
#
#     while col <= row:
#         print("*", end ="")
#
#         col += 1
#
#     print("")
#
#     row += 1


# #STEP 2
# row = 1
#
# while row <= 9:
#
#     col = 1
#
#     while col <= row:
#         # print("*", end ="")
#         print("9 * 9 = 81", end =" ")
#
#
#         col += 1
#
#     print("")
#
#     row += 1


#STEP 3
row = 1

while row <= 9:

    col = 1

    while col <= row:
        # print("*", end ="")
        print("%d * %d = %d"  % (col, row, col * row), end ="\t")


        col += 1

    print("")

    row += 1



