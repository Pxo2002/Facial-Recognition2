from tkinter import messagebox
from mysql.connector import Error
import mysql.connector
from cryptography.fernet import Fernet

def add_to_database(entry_1,entry_2,image_path):
   
    if (entry_1.get() == "" and entry_2.get() == "" and image_path==None):
        messagebox.showwarning("Empty Field!", "Please Fill all the required fields")
        return

    # Get the values from the entry fields
    name = entry_1.get()
    tp_number = entry_2.get()

    # Read the image file and convert it to a binary format
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Establish a connection to the MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='students',
            user='root',
            password=''
        )
        key = b'FwMO2y7T1iWUEhmaw3iVHn56jE09wjTMhrvBbUIoTLQ='
        cipher_suite = Fernet(key)
        if connection.is_connected():
            cursor = connection.cursor()

            name = cipher_suite.encrypt(name.encode())
            tp_number = cipher_suite.encrypt(tp_number.encode())
            # Prepare the INSERT statement
            insert_query = "INSERT INTO students (name, tp_number, image) VALUES (%s, %s, %s)"
            values = (name, tp_number, image_data)

            # Execute the INSERT statement
            cursor.execute(insert_query, values)

            # Commit the changes to the database
            connection.commit()

            messagebox.showinfo("Success!","Student inserted successfully!")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
