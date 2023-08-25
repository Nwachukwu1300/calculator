from tkinter import *


def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    
def button_dec():
    current = e.get()
    if "." not in current:
        e.insert(END,".")

def button_clear():
    e.delete(0,END)
    
def button_back():
    current = e.get()
    if current:
        e.delete(len(current) - 1)

def button_add():
    first_num = e.get()
    global f_num
    global math 
    math = "addition"
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0,END)
    

def button_equal():
    try:
        second_num = e.get()
        e.delete(0, END)
        if "." in second_num:
            second_num = float(second_num)
        else:
            second_num = int(second_num)
        if math == "addition":
            e.insert(0, f_num + second_num)
        if math == "subtraction":
            e.insert(0, f_num - second_num)
        if math == "multiply":
            e.insert(0, f_num * second_num)
        if math == "divide":
            e.insert(0, f_num / second_num)
    except Exception as math_error:
        e.delete(0,END)
        e.insert(0,"MATH ERROR")
        


def button_sub():
    first_num = e.get()
    global f_num
    global math 
    math = "subtraction"
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0,END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math 
    math = "multiply"
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0,END)


def button_divide():
    first_num = e.get()
    global f_num
    global math 
    math = "divide"
    if "." in first_num:
        f_num = float(first_num)
    else:
        f_num = int(first_num)
    e.delete(0,END)

# Define button labels and corresponding commands
button_specs = [
    ("7", lambda: button_click(7)),
    ("8", lambda: button_click(8)),
    ("9", lambda: button_click(9)),
    ("4", lambda: button_click(4)),
    ("5", lambda: button_click(5)),
    ("6", lambda: button_click(6)),
    ("1", lambda: button_click(1)),
    ("2", lambda: button_click(2)),
    ("3", lambda: button_click(3)),
    ("0", lambda: button_click(0)),
    ("+", button_add),
    ("-", button_sub),
    ("X", button_multiply),
    ("/", button_divide),
    ("=", button_equal),
    ("CLEAR", button_clear),
    ("⌫", button_back),
    (".", button_dec)
]

root = Tk()
root.title("Mmesoma's Calculator")

e = Entry(root, width=40, borderwidth=6)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create and place buttons using nested loops
row_start = 2
col_start = 0
for i, (label, command) in enumerate(button_specs):
    row = row_start + i // 4
    col = col_start + i % 4
    Button(root, text=label, padx=40, pady=20, command=command).grid(row=row, column=col, padx=10, pady=10)

root.mainloop()

