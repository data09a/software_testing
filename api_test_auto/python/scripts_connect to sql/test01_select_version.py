# import pymsyql
import pymysql

# connect to sql (the data below is mandatory)
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       database="books")


# 2nd version
# conn = pymysql.connect(host="127.0.0.1",
#                        user="root",
#                        password="123456",
#                        database="books",
#                        port=3306,
#                        charset="utf8",
#                        autocommit=False)

# ## 3rd version
# conn =pymysql.connect("127.0.0.1",
#                       "root",
#                       "123456",
#                       "books",
#                       3306,
#                       charset="utf8")



# get cursor
cursor = conn.cursor()

# get data
sql = "select version()"
num = cursor.execute(sql)
print("Return：", num)


# get result
result_one = cursor.fetchone()
print("Result：", result_one)

# close cursor
cursor.close()

# close connection
conn.close()