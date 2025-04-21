# pip install pymysql

import pymysql

try:
    connection = pymysql.connect(
        host="39.108.92.253",
        user="root",
        password="huangbaoze.com",
        database="rag_platform",
        port=3306
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM chunks")
        for row in cursor.fetchall():
            print(row)

    connection.close()

except Exception as e:
    print("数据库连接失败:", e)


