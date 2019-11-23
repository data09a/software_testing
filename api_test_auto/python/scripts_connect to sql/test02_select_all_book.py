

import pymysql

conn = pymysql.connect("127.0.0.1",
                       "root",
                       "123456",
                       "books",
                       3306,
                       charset="utf8")

# get cursor
cursor = conn.cursor()

# get all data from the table
sql = "select * from t_book"
cursor.execute(sql)

# count all books
num = cursor.rowcount
print("The total number of the book：", num)

# get the name of all books
# all = cursor.fetchall()
# print("books name：", all)
# print("Type：", type(all))

# print all the book
# for i in all:
#     print("book name：", i[1])


# fetch one data
one = cursor.fetchone()
print("one：", one)

# fetch 2 books info
size = cursor.fetchmany(2)
print("2 books info：", size)

cursor.close()

conn.close()
