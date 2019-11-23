
import pymysql


conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       database="books",
                       port=3306,
                       autocommit=True)


cursor = conn.cursor()


sql = "INSERT INTO t_book(title,pub_date) values ('book Alpha', '1980-1-3')"
cursor.execute(sql)

]
cursor.close()


conn.close()
