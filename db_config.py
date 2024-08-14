import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # 连接到 MySQL 服务器
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # 替换为你的 MySQL 用户名
            password='123456'  # 替换为你的 MySQL 密码
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS ")
            print("Database created successfully")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# def create_table():
#



if __name__ == 'main':
    create_database()
    # create_table()
