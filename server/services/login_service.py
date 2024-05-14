import mysql.connector
from services.connectionDB import connect_to_mysql

def get_user(username, password):
    connection = connect_to_mysql()
    if not connection:
        return None, 'Lỗi khi kết nối đến cơ sở dữ liệu.'
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM account WHERE name_account = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        return user, None
    except mysql.connector.Error as error:
        return None, 'Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu.'
    finally:
        cursor.close()
        connection.close()
