import datetime
from mysql.connector import Error
import mysql.connector


def insert_attendance(session_time):
    try:
        connection = mysql.connector.connect(
            host='srv1031.hstgr.io',
            database='u779400461_students',
            user='u779400461_admin',
            password='8@IZ?5HmYHe'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Retrieve all student IDs from the students table
            cursor.execute("SELECT id FROM students")
            student_ids = cursor.fetchall()
            # Insert the data into the attendance table for each student
            for student_id in student_ids:
                status = "Absent"
                course_id = "1"
                query = "INSERT INTO attendance (student_id, course_id, session_time, status) VALUES (%s, %s, %s, %s)"
                values = (student_id[0], course_id, session_time, status)
                cursor.execute(query, values)
                connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
