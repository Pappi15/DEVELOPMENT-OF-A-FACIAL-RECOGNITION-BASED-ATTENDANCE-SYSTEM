import tkinter as tk
from tkinter import StringVar, Label, Entry, W, END
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil
import sqlite3 as sl
from main import *

# Database connection
con = sl.connect('data.db')

# Main window setup
gin = tk.Tk()
gin.geometry("560x300")
gin.title('Facial Recognition based Identification System')

# Name
name_text = StringVar()
name_label = Label(gin, text='Name', font=('bold', 14), pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(gin, textvariable=name_text)
name_entry.grid(row=0, column=1)

# Matric Num
roll_text = StringVar()
roll_label = Label(gin, text='Matric Num', font=('bold', 14))
roll_label.grid(row=0, column=4, sticky=W)
roll_entry = Entry(gin, textvariable=roll_text)
roll_entry.grid(row=0, column=5)

# Image
img_label = Label(gin, text='Select Image', font=('bold', 14), pady=20)
img_label.grid(row=1, column=0, sticky=W)
upload_button = tk.Button(gin, text='Upload Files', command=lambda: upload_file())
upload_button.grid(row=1, column=1)

# Output
output_label = Label(gin, text='Added to DB', font=('bold', 14))

# Start camera operation
cam_button = tk.Button(gin, text='Start Cam', command=lambda: cctv())
cam_button.grid(row=9, column=1)

def clear_text(image_label, button):
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    output_label.configure(text="")
    image_label.config(image='')
    button.destroy()

def upload_file():
    file_types = [('Jpg Files', '*.jpg')]
    filenames = filedialog.askopenfilename(multiple=True, filetypes=file_types)
    col = 1
    row = 3
    for file in filenames:
        img = Image.open(file)
        roll = roll_text.get()
        sql = 'INSERT INTO USER (id, name, location) VALUES (?, ?, ?)'
        data = (roll, name_text.get(), 'Main Gate')
        with con:
            con.execute(sql, data)
        shutil.copy(file, f'images/{roll}.jpg')

        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)
        image_label = Label(gin, image=img)
        image_label.grid(row=row, column=col)
        image_label.image = img

        output_label.grid(row=7, column=1)
        add_new_button = tk.Button(gin, text='Add New', command=lambda: clear_text(image_label, add_new_button))
        add_new_button.grid(row=8, column=1)

        if col == 3:
            row += 1
            col = 1
        else:
            col += 1

gin.mainloop()
