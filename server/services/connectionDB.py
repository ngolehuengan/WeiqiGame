import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="weiqi",
            charset="utf8mb4"
        )
        if connection.is_connected():
            print('Kết nối đến cơ sở dữ liệu MySQL thành công.')
            return connection
    except Error as e:
        print('Lỗi khi kết nối đến cơ sở dữ liệu MySQL:', e)
        return None