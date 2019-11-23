import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="123456",
                       database="books",
                       port=3306)

cursor = conn.cursor()

# auto commit
# conn.autocommit(True)

try:

    sql_book = "insert into t_book(title,pub_date)values('book_Bravo','1986-1-1')"
    cursor.execute(sql_book)

    sql_hero = "insert into t_hero(name,gender,book_id)values('hero_B',1,4)"
    cursor.execute(sql_hero)

    # manual commit
    conn.commit()
except Exception as e:
    # print error info
    print(e)
    # rollback
    conn.rollback()

finally:
    cursor.close()

    conn.close()
