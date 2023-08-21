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

root = Tk()
root.title("Mmesoma's Calculator")

e = Entry(root, width=40,borderwidth=6)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtraction = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_multiplication = Button(root, text="X", padx=40, pady=20, command=button_multiply)
button_division = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_equalto = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clearpage = Button(root, text="CLEAR", padx=79, pady=20, command=button_clear)
button_backspace = Button(root, text="⌫", padx=40, pady=20, command=button_back)
button_decimal = Button(root, text=".", padx=40, pady=20, command=button_dec)



#put buttons on screen
button_1.grid(row=2, column=0, padx=10, pady=10)
button_2.grid(row=2, column=1, padx=10, pady=10)
button_3.grid(row=2, column=2, padx=10, pady=10)

button_4.grid(row=3, column=0, padx=10, pady=10)
button_5.grid(row=3, column=1, padx=10, pady=10)
button_6.grid(row=3, column=2, padx=10, pady=10)

button_7.grid(row=4, column=0, padx=10, pady=10)
button_8.grid(row=4, column=1, padx=10, pady=10)
button_9.grid(row=4, column=2, padx=10, pady=10)

button_0.grid(row=5, column=0, padx=10, pady=10)
button_addition.grid(row=2, column=3, padx=10, pady=10)
button_subtraction.grid(row=3, column=3, padx=10, pady=10)
button_multiplication.grid(row=4, column=3, padx=10, pady=10)
button_division.grid(row=5, column=3, padx=10, pady=10)

button_clearpage.grid(row=5, column=1, padx=10, pady=10)
button_backspace.grid(row=5, column=2, padx=10, pady=10)
button_equalto.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
button_decimal.grid(row=6, column=1, padx=10, pady=10)




root.mainloop()