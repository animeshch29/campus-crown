import tkinter as tk
from tkinter import ttk

# Initialize the main window
win = tk.Tk()
win.geometry('1350x700+0+0')
win.title('CAMPUS CROWN')

# Title

title_label = tk.Label(
    win,
    text='CAMPUS CROWN',
    font=('Pacifico', 30, 'bold'),
    borderwidth=12,
    relief=tk.GROOVE,
    bg='white',  
    fg='grey',  
)
title_label.pack(side=tk.TOP, fill=tk.X)
# Detail frame
detail_frame = tk.Frame(
    win, bd=12,
    relief=tk.GROOVE
)
detail_frame.place(x=20, y=90, width=420, height=575)

# Data frame
data_frame = tk.Frame(win, bd=12, bg='grey', relief=tk.GROOVE)
data_frame.place(x=420, y=90, width=810, height=575)

# Variables
rollno = tk.StringVar()
name = tk.StringVar()
clss = tk.StringVar()
email = tk.StringVar()
gender = tk.StringVar()
contact = tk.StringVar()
dob = tk.StringVar()
address = tk.StringVar()
search_by = tk.StringVar()

# Entry Fields
# Roll No
rollno_lbl = tk.Label(detail_frame, text="Roll No.", font=('Arial', 17), bg='grey')
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

rollno_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 17), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

# Name
name_lbl = tk.Label(detail_frame, text='Name', font=('Arial', 17), bg='grey')
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 17), textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

# Class
clss_lbl = tk.Label(detail_frame, text="Class", font=("Arial", 17), bg='grey')  
clss_lbl.grid(row=2, column=0, padx=2, pady=2)

clss_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 17), textvariable=clss)
clss_ent.grid(row=2, column=1, padx=2, pady=2)

# Email
email_lbl = tk.Label(detail_frame, text='E-mail', font=('Arial', 17), bg='grey')
email_lbl.grid(row=3, column=0, padx=2, pady=2)

email_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 17), textvariable=email)
email_ent.grid(row=3, column=1, padx=2, pady=2)

# Gender
gender_lbl = tk.Label(detail_frame, text='Gender', font=('Arial', 17), bg='grey')
gender_lbl.grid(row=4, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, font=('Arial', 17), textvariable=gender)  # Combobox used
gender_ent['values'] = ('Male', 'Female', 'Other')
gender_ent.grid(row=4, column=1, padx=2, pady=2)

# Contact
contact_lbl = tk.Label(detail_frame, text="Contact", font=('Arial', 17), bg='grey')
contact_lbl.grid(row=5, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 17), textvariable=contact)
contact_ent.grid(row=5, column=1, padx=2, pady=2)

# D.O.B
dob_lbl = tk.Label(detail_frame, text="D.O.B", font=('Arial', 17), bg='grey')
dob_lbl.grid(row=6, column=0, padx=2, pady=2)

dob_ent = tk.Entry(detail_frame, font=('Arial', 17), bd=7, textvariable=dob)
dob_ent.grid(row=6, column=1, padx=2, pady=2)

# Address
address_lbl = tk.Label(detail_frame, text="Address", font=('Arial', 17), bg='grey')
address_lbl.grid(row=7, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=6, font=('Arial', 17), width=20, textvariable=address)
address_ent.grid(row=7, column=1, padx=2, pady=2)

# Buttons
btn_frame = tk.Frame(detail_frame, bg='grey', bd=10, relief=tk.GROOVE)
btn_frame.place(x=20, y=390, width=370, height=120)

add_btn = tk.Button(btn_frame, bg='grey', text='Add', bd=7, font=('Arial', 13), width=10)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg='grey', text='Update', bd=7, font=('Arial', 13), width=10)
update_btn.grid(row=0, column=1, padx=2, pady=2)

delete_btn = tk.Button(btn_frame, bg='grey', text='Delete', bd=7, font=('Arial', 13), width=10)
delete_btn.grid(row=1, column=0, padx=10, pady=10)

clear_btn = tk.Button(btn_frame, bg='grey', text='Clear', bd=7, font=('Arial', 13), width=10)
clear_btn.grid(row=1, column=1, padx=10, pady=10)

# Search Frame
search_frame = tk.Frame(data_frame, bg='grey', bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text='Search', bg='grey', font=('Arial', 14))
search_lbl.grid(row=0, column=0, padx=7, pady=2)

search_in = ttk.Combobox(search_frame, font=('Arial', 14), state='readonly')
search_in['values'] = ('Name', 'Roll No', 'Contact', 'Class', 'D.O.B')  
search_in.grid(row=0, column=1, padx=7, pady=2)

search_btn = tk.Button(search_frame, text='Search', font=('Arial', 13), bd=9, width=14, bg='lightgrey')
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text='Show All', font=('Arial', 13), bd=9, width=14, bg='lightgrey')
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# Database frame
main_frame = tk.Frame(data_frame, bg='lightgrey', relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

# Scrollbars
y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# Treeview
student_table = ttk.Treeview(main_frame, columns=('Roll No', 'Name', 'Class', 'E-mail', 'Gender', 'D.O.B', 'Contact', 'Address'), 
                               yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

# Configure scrollbars
y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Treeview headings
student_table.heading('Roll No', text='Roll No')
student_table.heading('Name', text='Name')
student_table.heading('Class', text='Class')
student_table.heading('E-mail', text='E-mail')
student_table.heading('Gender', text='Gender')
student_table.heading('D.O.B', text='D.O.B')
student_table.heading('Contact', text='Contact')
student_table.heading('Address', text='Address')
student_table['show'] = 'headings'

# Treeview columns
student_table.column('Roll No', width=100)
student_table.column('Name', width=100)
student_table.column('Class', width=100)
student_table.column('E-mail', width=100)
student_table.column('Gender', width=100)
student_table.column('D.O.B', width=100)
student_table.column('Contact', width=100)
student_table.column('Address', width=150)

student_table.pack(fill=tk.BOTH, expand=True)

# Run the application
win.mainloop()
