import datetime
import random
from tkinter import LEFT, Frame, Label, Spinbox, Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
from pathlib import Path
import tkinter
from urllib.parse import urlencode
from PIL import ImageTk, Image
import qrcode
from tkcalendar import DateEntry
import tkinter as tk
import pandas as pd
from tkinter import CENTER, ttk
from tkinter import filedialog
import mysql.connector
from twilio.rest import Client
from cryptography.fernet import Fernet

from addStudents import add_to_database
from makeAttendance import insert_attendance

OUTPUT_PATH = Path(__file__).parent
path = "C:\\Users\\Saiid\\Desktop\\Student Updated\\assets"

LOGIN_PAGE_ASSETS_PATH = OUTPUT_PATH / \
    Path(rf"{path}\\login")
TWO_FACTORS_PAGE_ASSETS_PATH = OUTPUT_PATH / \
    Path(rf"{path}\\two_factors")
HOME_PAGE_ASSETS_PATH = OUTPUT_PATH / \
    Path(rf"{path}\\home")
ADD_STUDENTS_PAGE_ASSETS_PATH = OUTPUT_PATH / \
    Path(rf"{path}\\add_students")

image_path = None
qr_image = None 
session_time = None
otp = None

def relative_to_assets(path: str, assets_path: Path) -> Path:
    return assets_path / Path(path)

# def open_login_page():
#     global window

#     login_page()
    
# def open_two_factors_page():
#     global window

#     window.destroy()
#     two_factors_page()
    
def open_home_page():
    global window
    if hasattr(window, 'generate_otp_id'):
        # Cancel the scheduled function
        window.after_cancel(window.generate_otp_id)
    window.destroy()
    home_page()
    
def open_add_students_page():
    global window

    window.destroy()
    add_students_page()
    
def open_students_page():
    global window

    window.destroy()
    display_students_page()
def open_qr_generator_page():
    global window

    window.destroy()
    qr_generator_page()

def exit():
    global window
    
    window.destroy()
    
# def login_page():
#     global window 
#     window = Tk()

#     window.geometry("550x313")
#     window.configure(bg = "#FFFFFF")


#     canvas = Canvas(
#         window,
#         bg = "#FFFFFF",
#         height = 313,
#         width = 550,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge"
#     )

#     canvas.place(x = 0, y = 0)
#     canvas.create_text(
#         167.0,
#         27.0,
#         anchor="nw",
#         text="Login Page",
#         fill="#000000",
#         font=("Inter", 24 * -1)
#     )

#     canvas.create_text(
#         53.0,
#         74.0,
#         anchor="nw",
#         text="Username:",
#         fill="#000000",
#         font=("Inter", 16 * -1)
#     )

#     button_image_1 = PhotoImage(
#         file=relative_to_assets("button_1.png",LOGIN_PAGE_ASSETS_PATH))
#     button_1 = Button(
#         image=button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: open_two_factors_page(),
#         relief="flat"
#     )
#     button_1.place(
#         x=210.0,
#         y=240.0,
#         width=131.0,
#         height=37.0
#     )

#     entry_image_1 = PhotoImage(
#         file=relative_to_assets("entry_1.png", LOGIN_PAGE_ASSETS_PATH))
#     entry_bg_1 = canvas.create_image(
#         175.0,
#         113.5,
#         image=entry_image_1
#     )
#     entry_1 = Entry(
#         bd=0,
#         bg="#F5F5F5",
#         fg="#000716",
#         highlightthickness=0
#     )
#     entry_1.place(
#         x=53.0,
#         y=100.0,
#         width=244.0,
#         height=25.0
#     )

#     canvas.create_text(
#         53.0,
#         145.0,
#         anchor="nw",
#         text="Password:",
#         fill="#000000",
#         font=("Inter", 16 * -1)
#     )

#     entry_image_2 = PhotoImage(
#         file=relative_to_assets("entry_2.png", LOGIN_PAGE_ASSETS_PATH))
#     entry_bg_2 = canvas.create_image(
#         175.0,
#         183.5,
#         image=entry_image_2
#     )
#     entry_2 = Entry(
#         bd=0,
#         bg="#F5F5F5",
#         fg="#000716",
#         highlightthickness=0
#     )
#     entry_2.place(
#         x=53.0,
#         y=170.0,
#         width=244.0,
#         height=25.0
#     )
#     window.resizable(False, False)
#     window.mainloop()

# def two_factors_page():
#     global window
#     window = Tk()

#     window.geometry("550x313")
#     window.configure(bg="#FFFFFF")

#     n = random.randint(1000,9999)
#     client = Client("AC70bdeb38d7de4903c4e58e9478726755",
#                     "bec83e2ee1ab7a364617db1a8fdf081f")
#     client.messages.create(to=["+96171933262"], from_="+96178929281", body=n)
#     def resendSMS():
#         n = random.randint(1000, 9999)
#         client = Client("", "")
#         client.messages.create(to=[""], from_="", body=n)
    
#     canvas = Canvas(
#         window,
#         bg="#FFFFFF",
#         height=313,
#         width=550,
#         bd=0,
#         highlightthickness=0,
#         relief="ridge"
#     )

#     canvas.place(x=0, y=0)
#     canvas.create_text(
#         136.0,
#         25.0,
#         anchor="nw",
#         text="Two-Factor Authentication",
#         fill="#000000",
#         font=("Inter", 24 * -1)
#     )

#     canvas.create_text(
#         46.0,
#         109.0,
#         anchor="nw",
#         text="Enter the sms Here:",
#         fill="#000000",
#         font=("Inter", 16 * -1)
#     )

#     button_image_1 = PhotoImage(
#         file=relative_to_assets("button_1.png",TWO_FACTORS_PAGE_ASSETS_PATH))
#     button_1 = Button(
#         image=button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_1 clicked"),
#         relief="flat"
#     )
#     button_1.place(
#         x=323.0,
#         y=195.0,
#         width=131.0,
#         height=37.0
#     )

#     button_image_2 = PhotoImage(
#         file=relative_to_assets("button_2.png", TWO_FACTORS_PAGE_ASSETS_PATH))
#     button_2 = Button(
#         image=button_image_2,
#         borderwidth=0,
#         highlightthickness=0,
#         command=lambda: print("button_2 clicked"),
#         relief="flat"
#     )
#     button_2.place(
#         x=46.0,
#         y=200.0,
#         width=131.0,
#         height=37.0
#     )

#     entry_image_1 = PhotoImage(
#         file=relative_to_assets("entry_1.png", TWO_FACTORS_PAGE_ASSETS_PATH))
#     entry_bg_1 = canvas.create_image(
#         332.0,
#         120.5,
#         image=entry_image_1
#     )
#     entry_1 = Entry(
#         bd=0,
#         bg="#F5F5F5",
#         fg="#000716",
#         highlightthickness=0
#     )
#     entry_1.place(
#         x=210.0,
#         y=107.0,
#         width=244.0,
#         height=25.0
#     )

#     def checkSMS():
#         try:
#             input = int(entry_1.get(1.0,"end-1c"))
#             if(input==n):
#                 open_home_page()
#             else:
#                 messagebox.showinfo("Failed!","Wrong SMS")
#         except:
#             messagebox.showinfo("Invalid!","Invalid SMS")
#     window.resizable(False, False)
#     window.mainloop()

def home_page():
    global window
    
    window = Tk()

    window.geometry("550x410")
    window.configure(bg="#FFFFFF")


    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=410,
        width=550,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        204.0,
        23.0,
        anchor="nw",
        text="Home Page",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png",HOME_PAGE_ASSETS_PATH))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:open_add_students_page(),
        relief="flat"
    )
    button_1.place(
        x=81.0,
        y=101.0,
        width=123.0,
        height=88.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png",HOME_PAGE_ASSETS_PATH))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_students_page(),
        relief="flat"
    )
    button_2.place(
        x=346.0,
        y=101.0,
        width=123.0,
        height=88.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png",HOME_PAGE_ASSETS_PATH))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_qr_generator_page(),
        relief="flat"
    )
    button_3.place(
        x=81.0,
        y=238.0,
        width=123.0,
        height=88.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png",HOME_PAGE_ASSETS_PATH))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_4.place(
        x=346.0,
        y=238.0,
        width=123.0,
        height=88.0
    )
    window.resizable(False, False)
    window.mainloop()
def add_students_page():
    
    def select_file():
        global image_path
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

        # Store the selected file path
        image_path=file_path
        
    global window
    window = Tk()

    window.geometry("550x410")
    window.configure(bg="#FFFFFF")


    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=410,
        width=550,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        167.0,
        27.0,
        anchor="nw",
        text="Add Students",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    canvas.create_text(
        53.0,
        64.0,
        anchor="nw",
        text="Student Name:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png",ADD_STUDENTS_PAGE_ASSETS_PATH))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_func(),
        relief="flat"
    )
    button_1.place(
        x=373.0,
        y=351.0,
        width=131.0,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png", ADD_STUDENTS_PAGE_ASSETS_PATH))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_home_page(),
        relief="flat"
    )
    button_2.place(
        x=53.0,
        y=351.0,
        width=131.0,
        height=37.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png", ADD_STUDENTS_PAGE_ASSETS_PATH))
    entry_bg_1 = canvas.create_image(
        175.0,
        103.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F5F5F5",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=53.0,
        y=90.0,
        width=244.0,
        height=25.0
    )

    canvas.create_text(
        53.0,
        135.0,
        anchor="nw",
        text="Tp Number:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png", ADD_STUDENTS_PAGE_ASSETS_PATH))
    entry_bg_2 = canvas.create_image(
        175.0,
        173.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F5F5F5",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=53.0,
        y=160.0,
        width=244.0,
        height=25.0
    )

    canvas.create_text(
        53.0,
        273.0,
        anchor="nw",
        text="Student Image:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png", ADD_STUDENTS_PAGE_ASSETS_PATH))
    entry_bg_4 = canvas.create_image(
        175.0,
        311.5,
        image=entry_image_4
    )

    # Create a button for selecting an image
    button_3 = Button(text="Select Image", command=select_file)
    button_3.pack()
    button_3.place(
        x=53.0,
        y=298.0,
        width=244.0,
        height=25.0
    )
    def show_func():
        add_to_database(entry_1,entry_2,image_path)
    window.resizable(False, False)
    window.mainloop()


def display_students_page():
    global window
    key = b'FwMO2y7T1iWUEhmaw3iVHn56jE09wjTMhrvBbUIoTLQ='
    cipher_suite = Fernet(key)
    window = tk.Tk()
    window.title("Students Page")

    # Connect to MySQL database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="students"
    )

    cursor = cnx.cursor()

    # Fetch data from the attendance table with student and course names
    cursor.execute("""
        SELECT attendance.id, students.name AS student_name, courses.course_name, attendance.status, attendance.session_time
        FROM attendance
        INNER JOIN students ON attendance.student_id = students.id
        INNER JOIN courses ON attendance.course_id = courses.id
    """)

    attendance_columns = ['ID', 'Student Name',
                          'Course Name', 'Status', 'Session Time']

    attendance_data = cursor.fetchall()

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(attendance_data, columns=attendance_columns)
    df.sort_values(by='Session Time', inplace=True)

    def populate_table():
        for i, row in df.iterrows():
            # Decrypt the student name
            decrypted_name = cipher_suite.decrypt(row['Student Name']).decode()

            # Replace the encrypted name with the decrypted name in the row
            row['Student Name'] = decrypted_name

            table.insert('', 'end', values=row.tolist())

    def search_records():
        search_term = search_var.get()
        search_results = df[df['Student Name'].str.contains(
            search_term, case=False)]
        table.delete(*table.get_children())
        for i, row in search_results.iterrows():
            # Decrypt the student name
            decrypted_name = cipher_suite.decrypt(row['Student Name']).decode()

            # Replace the encrypted name with the decrypted name in the row
            row['Student Name'] = decrypted_name

            table.insert('', 'end', values=row.tolist())


    def export_to_excel():
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if file_path:
            export_df = df if search_var.get(
            ) == '' else df[df['Student Name'].str.contains(search_var.get(), case=False)]
            export_df.to_excel(file_path, index=False)

    search_var = tk.StringVar()

    title_label = ttk.Label(window, text="Students Page",
                            font=("Arial", 16, "bold"))
    # Add title label at the top
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    search_entry = ttk.Entry(window, textvariable=search_var)
    # Add padding to the right side
    search_entry.grid(row=1, column=0, padx=(100, 80), sticky=tk.E)

    search_button = ttk.Button(window, text="Search", command=search_records)
    # Position the button next to the search input
    search_button.grid(row=1, column=0,  padx=(970, 0), sticky=tk.E)

    back_button = ttk.Button(window, text="Back", command=open_home_page)
    # Position the button in the top right corner
    back_button.grid(row=0, column=2, sticky=tk.NE)

    table = ttk.Treeview(window, columns=attendance_columns,
                         show='headings', displaycolumns=attendance_columns)
    for i, column in enumerate(attendance_columns):
        if column == 'course_name':
            table.heading(i, text='Course Name')
        else:
            table.heading(i, text=column.title())
        table.column(i, anchor=tk.CENTER)  # Center the text in each column

    table.grid(row=2, column=0, columnspan=3)

    export_button = ttk.Button(
        window, text="Export to Excel", command=export_to_excel)
    export_button.grid(row=3, column=0, columnspan=3)

    populate_table()

    window.mainloop()

def qr_generator_page():
    global window
    window = Tk()
    window.title("QR Code Generator")


    def get_date_time():
        global session_time
        date = date_entry.get()
        hour = hour_entry.get()
        minute = minute_entry.get()
        session_time_str = f"{date} {hour}:{minute}:0"
        session_time_format = datetime.datetime.strptime(
            session_time_str, "%m/%d/%y %H:%M:%S")
        session_time = session_time_format.strftime("%Y-%m-%d %H:%M:%S")

        session_time_label.configure(text=f"Session Time: {session_time}")

        insert_attendance(session_time)

    header_label = Label(window, text="QR Code Generator",
                         font=("Arial", 16, "bold"))

    header_label.pack(pady=10)

    date_frame = Frame(window)
    date_frame.pack()

    date_label = Label(date_frame, text="Date:")
    date_label.pack(side=LEFT, padx=10, pady=10)

    date_entry = DateEntry(
        date_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.pack(side=LEFT, padx=10, pady=10)

    time_frame = Frame(window)
    time_frame.pack()

    time_label = Label(time_frame, text="Time (HH:MM):")
    time_label.pack(side=LEFT, padx=10, pady=10)

    hour_entry = Spinbox(time_frame, from_=0, to=23, width=3, state="readonly")
    hour_entry.pack(side=LEFT, padx=(10, 0), pady=10)

    minute_entry = Spinbox(time_frame, from_=0, to=59, width=3, state="readonly")
    minute_entry.pack(side=LEFT, padx=(5, 10), pady=10)

    submit_button = Button(window, text="Submit", command=get_date_time)
    submit_button.pack(padx=10, pady=10)
    session_time_label = Label(window, text="", font=(
        "Arial", 12), borderwidth=2, relief="solid", bg="lightblue", fg="black")
    session_time_label.pack(pady=5)

    otp_label = Label(window, text="", font=("Arial", 14))
    otp_label.pack(pady=10)
    def update_otp(otp):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='students'
        )
        cursor = conn.cursor()

        query = "UPDATE courses SET otp = %s WHERE id = 1"
        cursor.execute(query, (otp,))

        conn.commit()
        conn.close()
    def generate_otp():
        global otp
        if window.winfo_exists():  # Check if the window is still active
            otp = random.randint(100000, 999999)
            otp_label.configure(text=f"OTP: {otp}")
            update_otp(otp)
            if hasattr(window, 'generate_otp_id'):
                window.after_cancel(window.generate_otp_id)
            # Start a new after() call
            window.generate_otp_id = window.after(
                30000, generate_otp)  # Schedule the next execution

    generate_otp()
    
    label = Label(
        window, text="Click the button to generate QR code", font=("Arial", 12))
    label.pack()

    # Frame for centering the button
    button_frame = Frame(window)
    button_frame.pack()


    def generate_qr_code():
        global session_time
        if(session_time==None):
            messagebox.showerror("Error", "Please enter session time")
            return
        url_encoded_session_time = urlencode(
            {"session_time": session_time})
        print(url_encoded_session_time)
        message = f"https://www.google.com?{url_encoded_session_time}"
        if message:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(message)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save('qr_code.png')
            show_qr_code()

    def show_qr_code():
        global qr_image
        if qr_image:
            try:
                qr_image.destroy()  # Destroy previous image object if exists
            except tkinter.TclError:
                pass

        qr_image = Label(window)
        qr_image.pack()

        image = ImageTk.PhotoImage(Image.open('qr_code.png'))
        qr_image.configure(image=image)
        qr_image.image = image  # Store a reference to avoid garbage collection issue
    button1 = Button(button_frame, text="Generate",
                    command=generate_qr_code)
    button1.pack(pady=10)
    button2 = Button(button_frame, text="Back",
                    command=open_home_page)
    button2.pack(pady=10)
    
#login_page()
home_page()