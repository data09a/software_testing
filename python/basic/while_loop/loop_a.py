#requirements:
#print 5 row of *, and +1 in the next row

#STEP 1

# row = 1
#
# while row <= 5:
#     print("row number %d" % row)
#
#     row += 1

# STEP 2

# row = 1
#
# while row <= 5:
#
#     col = 1
#
#     while col <= row:
#         print("%d" % col )
#
#         col += 1
#     print("row number %d" % row)
#
#     row += 1


# STEP 3
row = 1

while row <= 5:

    col = 1

    while col <= row:
        print("*", end ="")

        col += 1
    # print("row number %d" % row)
    print("")

    row += 1