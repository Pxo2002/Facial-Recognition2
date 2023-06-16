from tkinter import messagebox
from mysql.connector import Error
import mysql.connector
from cryptography.fernet import Fernet


def add_to_database(entry_1, entry_2, image_path):

    if (entry_1.get() == "" and entry_2.get() == "" and image_path == None):
        messagebox.showwarning(
            "Empty Field!", "Please Fill all the required fields")
        return

    name = entry_1.get()
    tp_number = entry_2.get()

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    try:
        connection = mysql.connector.connect(
            host='srv1031.hstgr.io',
            database='u779400461_students',
            user='u779400461_admin',
            password='8@IZ?5HmYHe'
        )
        key = b'FwMO2y7T1iWUEhmaw3iVHn56jE09wjTMhrvBbUIoTLQ='
        cipher_suite = Fernet(key)
        if connection.is_connected():
            cursor = connection.cursor()

            name = cipher_suite.encrypt(name.encode())
            tp_number = cipher_suite.encrypt(tp_number.encode())

            insert_query = "INSERT INTO students (name, tp_number, image) VALUES (%s, %s, %s)"
            values = (name, tp_number, image_data)

            cursor.execute(insert_query, values)

            connection.commit()

            messagebox.showinfo("Success!", "Student inserted successfully!")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
