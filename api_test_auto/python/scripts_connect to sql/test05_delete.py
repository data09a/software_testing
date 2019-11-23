


import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       database="books",
                       port=3306,
                       autocommit=True)


cursor = conn.cursor()

sql = "delete from t_book where title='book Alpha'"
cursor.execute(sql)


cursor.close()


conn.close()
