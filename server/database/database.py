import mysql.connector
from flask import Flask, request, jsonify

def connect_to_mysql(host, username, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Kết nối thành công đến MySQL")

            return connection
        else:
            print("Không thể kết nối đến MySQL")
            return None

    except mysql.connector.Error as e:
        print("Lỗi kết nối đến MySQL:", e)
        return None

host = "localhost"
username = "root"
password = ""
database = "weiqi"

connection = connect_to_mysql(host, username, password, database)


if connection is not None:

    connection.close()
    print("Đã đóng kết nối đến MySQL")

    ##############################################    
class Acc:
    app = Flask(__name__)
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json
        username = data.get('username')
        password = data.get('password')
        connection = connect_to_mysql(host="localhost", username="root", password="", database="weiqi")

        if connection is not None:
            cursor = connection.cursor()

            # Truy vấn cơ sở dữ liệu để kiểm tra thông tin đăng nhập
            query = "SELECT * FROM account WHERE name_account = %s AND password = %s"
            cursor.execute(query, (username, password))
            #user = cursor.fetchone()

        #     if user:
        #         return jsonify({"message": "Login successful"})
        #     else:
        #         return jsonify({"error": "Invalid username or password"}), 401

        # else:
        #     return jsonify({"error": "Could not connect to database"}), 500

    if __name__ == '__main__':
        app.run(debug=True)
    