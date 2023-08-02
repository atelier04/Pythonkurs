import math
import tkinter
from tkinter import messagebox, W
from tkinter import Image, Button
from tkinter.messagebox import askyesno

# Window and textBox declaration
window = tkinter.Tk()
window.title("Rechner")
window.geometry("550x600")
textBox = tkinter.Text(window, height=3)
# Make textbox not editable through keystrokes
textBox.bind("<Key>", lambda e: "break")
textBox.pack(padx=20, pady=10)

frame = tkinter.Frame(window, bg="blue", width=500, height=10)

textBox_content = ''
math_operation = ''


# Declaration of functions to insert, calculate and delete numbers in the textbox.

def insert(number):
    if number == "0":
        if not len(textBox.get(1.0, "end").strip()) == 0:
            textBox.insert("end", number)
    else:
        textBox.insert("end", number)


def save(operation):
    global textBox_content
    global math_operation
    math_operation = operation
    textBox_content = textBox.get(1.0, "end")
    print(textBox_content)
    textBox.delete(1.0, "end")


def equals():
    erg = ""
    if math_operation == "add":
        erg = float(textBox_content) + float(textBox.get(1.0, "end"))
    elif math_operation == "sub":
        erg = float(textBox_content) - float(textBox.get(1.0, "end"))
    elif math_operation == "multiply":
        erg = float(textBox_content) * float(textBox.get(1.0, "end"))
    elif math_operation == "divide":
        erg = float(textBox_content) / float(textBox.get(1.0, "end"))
    else:
        print("unknown operation")
        raise (Exception("unknown operation"))

    textBox.delete(1.0, "end")
    textBox.insert(1.0, erg)


def clear():
    textBox.delete(1.0, "end")


def sqrt_calculate():
    if len(textBox.get(1.0, "end").strip()) >= 1:
        erg = math.sqrt(float(textBox.get(1.0, "end")))
        textBox.delete(1.0, "end")
        textBox.insert(1.0, erg)


def inv_sign():
    if textBox.get(1.0) != "-":
        textBox.insert(1.0, "-")
    else:
        textBox.delete(1.0)


def window_closing():
    yesorno = askyesno("Do you want to quit?", "By Confirming the application will be closed!!")
    if yesorno:
        window.destroy()
    else:
        print("The window will not be closed")


# Generate the frame and the grid for the buttons

button_1 = Button(frame, text="1", command=lambda: insert("1"))
button_1.grid(column=0, row=0, padx=5, pady=10, ipadx=65, ipady=10)
button_2 = Button(frame, text="2", command=lambda: insert("2"))
button_2.grid(column=1, row=0, padx=5, pady=10, ipadx=65, ipady=10)
button_3 = Button(frame, text="3", command=lambda: insert("3"))
button_3.grid(column=2, row=0, padx=5, pady=10, ipady=10, ipadx=65)

button_4 = Button(frame, text="4", command=lambda: insert("4"))
button_4.grid(column=0, row=1, padx=5, pady=10, ipadx=65, ipady=10)
button_5 = Button(frame, text="5", command=lambda: insert("5"))
button_5.grid(column=1, row=1, padx=5, pady=10, ipadx=65, ipady=10)
button_6 = Button(frame, text="6", command=lambda: insert("6"))
button_6.grid(column=2, row=1, padx=5, pady=10, ipady=10, ipadx=65)

button_7 = Button(frame, text="7", command=lambda: insert("7"))
button_7.grid(column=0, row=2, padx=5, pady=10, ipadx=65, ipady=10)
button_8 = Button(frame, text="8", command=lambda: insert("8"))
button_8.grid(column=1, row=2, padx=5, pady=10, ipadx=65, ipady=10)
button_9 = Button(frame, text="9", command=lambda: insert("9"))
button_9.grid(column=2, row=2, padx=5, pady=10, ipady=10, ipadx=65)

button_save = Button(frame, text="+", command=lambda: save("add"))
button_save.grid(column=0, row=3, padx=5, pady=20, ipady=10, ipadx=65)

button_sub = Button(frame, text="-", command=lambda: save("sub"))
button_sub.grid(column=1, row=3, padx=5, pady=10, ipady=10, ipadx=65)

button_multiply = Button(frame, text="*", command=lambda: save("multiply"))
button_multiply.grid(column=2, row=3, padx=5, pady=10, ipady=10, ipadx=65)

button_divide = Button(frame, text="/", command=lambda: save("divide"))
button_divide.grid(column=0, row=4, padx=5, pady=10, ipady=10, ipadx=65)

button_equals = Button(frame, text="=", command=lambda: equals())
button_equals.grid(column=1, row=4, padx=5, pady=10, ipady=10, ipadx=65)

button_clear = Button(frame, text="Clear", command=lambda: clear())
button_clear.grid(column=2, row=4, padx=5, pady=10, ipady=10, ipadx=55)

button_sqrt = Button(frame, text="Sqrt", command=lambda: sqrt_calculate())
button_sqrt.grid(column=0, row=5, padx=5, pady=10, ipady=10, ipadx=55)

button_zero = Button(frame, text="0", command=lambda: insert("0"))
button_zero.grid(column=1, row=5, padx=5, pady=10, ipady=10, ipadx=65)

button_neg_sign = Button(frame, text="Neg", command=lambda: inv_sign())
button_neg_sign.grid(column=2, row=5, padx=5, pady=10, ipady=10, ipadx=55)

frame.pack(pady=20, padx=10)

# Set window resizable to false and configure the behaviour for the cross in the top right corner

window.resizable(width=False, height=False)
window.protocol("WM_DELETE_WINDOW", window_closing)

window.mainloop()
