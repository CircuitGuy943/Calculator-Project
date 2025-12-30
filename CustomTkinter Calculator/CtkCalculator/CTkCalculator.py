import tkinter as tk
import customtkinter as ctk
from time import sleep

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("215x280")
root.resizable(False, False)

if True:
    def number1():
        entry.insert(tk.END, "1")
        print("1")


    def number2():
        entry.insert(tk.END, "2")
        print("2")


    def number3():
        print("3")
        entry.insert(tk.END, "3")


    def number4():
        print("4")
        entry.insert(tk.END, "4")


    def number5():
        entry.insert(tk.END, "5")
        print("5")


    def number6():
        entry.insert(tk.END, "6")
        print("6")


    def number7():
        entry.insert(tk.END, "7")
        print("7")


    def number8():
        entry.insert(tk.END, "8")
        print("8")


    def number9():
        entry.insert(tk.END, "9")
        print("9")


    def number0():
        entry.insert(tk.END, "0")
        print("0")


def add():
    entry_value = entry.get()
    if str(entry_value[len(entry.get()) - 1]) != "÷" and str(entry_value[len(entry.get()) - 1]) != "+" and str(
            entry_value[len(entry.get()) - 1]) != "-" and str(entry_value[len(entry.get()) - 1]) != "x":
        entry.insert(tk.END, "+")
        print("add")


def multiply():
    entry_value = entry.get()
    if str(entry_value[len(entry.get()) - 1]) != "÷" and str(entry_value[len(entry.get()) - 1]) != "+" and str(
            entry_value[len(entry.get()) - 1]) != "-" and str(entry_value[len(entry.get()) - 1]) != "x":
        entry.insert(tk.END, "*")
        print("multiply")


def takeaway():
    entry_value = entry.get()
    if str(entry_value[len(entry.get()) - 1]) != "÷" and str(entry_value[len(entry.get()) - 1]) != "+" and str(
            entry_value[len(entry.get()) - 1]) != "-" and str(entry_value[len(entry.get()) - 1]) != "x":
        entry.insert(tk.END, "-")
        print("takeaway")


def divide():
    entry_value = entry.get()
    if str(entry_value[len(entry.get()) - 1]) != "÷" and str(entry_value[len(entry.get()) - 1]) != "+" and str(
            entry_value[len(entry.get()) - 1]) != "-" and str(entry_value[len(entry.get()) - 1]) != "x":
        entry.insert(tk.END, "/")
        print("divide")


def solve():
    valid = 1
    unknown_character_warning = 0
    entry_value = entry.get()
    if (str(entry_value[len(entry.get()) - 1]) == "÷" or
            str(entry_value[len(entry.get()) - 1]) == "+" or
            str(entry_value[len(entry.get()) - 1]) == "-" or
            str(entry_value[len(entry.get()) - 1]) == "x" or
            str(entry_value[len(entry.get()) - 1]) == "^" or
            str(entry_value[0]) == "÷" or
            str(entry_value[0]) == "+" or
            str(entry_value[0]) == "-" or
            str(entry_value[0]) == "x" or
            str(entry_value[0]) == "^"):

        entry.delete(0, tk.END)
        entry.insert(0, "Unfinished Equation")
        entry.configure(state="readonly")
        entry.configure(font=("Arial", 20))
        root.update_idletasks()
        sleep(1)
        entry.configure(state="normal")
        entry.configure(font=("Arial", 25))
        entry.delete(0, tk.END)
        entry.insert(0, entry_value)
        valid = 0

    for x in entry_value:
        if x not in "0123456789+-*/^":
            valid = 0
            unknown_character_warning = 1

    if unknown_character_warning == 1:
        entry.delete(0, tk.END)
        entry.insert(0, "Unknown Character")
        entry.configure(state="readonly")
        entry.configure(font=("Arial", 20))
        root.update_idletasks()
        sleep(1)
        entry.configure(state="normal")
        entry.configure(font=("Arial", 25))
        entry.delete(0, tk.END)
        entry.insert(0, entry_value)

    if valid == 1:
        numbers_try = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        equation = "qwe" + entry_value + "qwe"

        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
        result = 0

        while "*" in equation:
            index_of_symbol = equation.index("*")
            while equation[index_of_symbol - count1] in numbers_try:
                count1 += 1
            while equation[index_of_symbol + count2] in numbers_try:
                count2 += 1
            num1 = equation[index_of_symbol - count1 + 1:index_of_symbol]
            num2 = equation[index_of_symbol + 1:index_of_symbol + count2]
            result = int(num1) * int(num2)
            equation = equation.replace(num1 + equation[index_of_symbol] + num2, str(int(result)))

        while "/" in equation:
            index_of_symbol = equation.index("/")
            while equation[index_of_symbol - count1] in numbers_try:
                count1 += 1
            while equation[index_of_symbol + count2] in numbers_try:
                count2 += 1
            num1 = equation[index_of_symbol - count1 + 1:index_of_symbol]
            num2 = equation[index_of_symbol + 1:index_of_symbol + count2]
            result = int(num1) / int(num2)
            equation = equation.replace(num1 + equation[index_of_symbol] + num2, str(round(result)))
            
        while "+" in equation:
            index_of_symbol = equation.index("+")
            while equation[index_of_symbol - count1] in numbers_try:
                count1 += 1
            while equation[index_of_symbol + count2] in numbers_try:
                count2 += 1
            num1 = equation[index_of_symbol - count1 + 1:index_of_symbol]
            num2 = equation[index_of_symbol + 1:index_of_symbol + count2]
            result = int(num1) + int(num2)
            equation = equation.replace(num1 + equation[index_of_symbol] + num2, str(int(result)))
            
        while "-" in equation:
            index_of_symbol = equation.index("-")
            while equation[index_of_symbol - count1] in numbers_try:
                count1 += 1
            while equation[index_of_symbol + count2] in numbers_try:
                count2 += 1
            num1 = equation[index_of_symbol - count1 + 1:index_of_symbol]
            num2 = equation[index_of_symbol + 1:index_of_symbol + count2]
            result = int(num1) - int(num2)
            equation = equation.replace(num1 + equation[index_of_symbol] + num2, str(int(result)))    
            
        entry.delete(0, tk.END)
        entry.insert(0, equation[3:-3])
        root.update_idletasks()
        print("rewritten entry")
        print(equation)


entry = ctk.CTkEntry(master=root, placeholder_text="Type Here", height=50, width=200, font=("Arial", 25))
entry.grid(column=0, row=0, columnspan=50, pady=10, padx=2)

button7 = ctk.CTkButton(master=root, text="7", command=number7, width=50, height=50)
button7.grid(column=0, row=1, padx=1, pady=1)
button8 = ctk.CTkButton(master=root, text="8", command=number8, width=50, height=50)
button8.grid(column=1, row=1, padx=1, pady=1)
button9 = ctk.CTkButton(master=root, text="9", command=number9, width=50, height=50)
button9.grid(column=2, row=1, padx=1, pady=1)
buttonx = ctk.CTkButton(master=root, text="*", command=multiply, width=50, height=50)
buttonx.grid(column=3, row=1, padx=1, pady=1)

button7 = ctk.CTkButton(master=root, text="7", command=number7, width=50, height=50)
button7.grid(column=0, row=1, padx=1, pady=1)
button8 = ctk.CTkButton(master=root, text="8", command=number8, width=50, height=50)
button8.grid(column=1, row=1, padx=1, pady=1)
button9 = ctk.CTkButton(master=root, text="9", command=number9, width=50, height=50)
button9.grid(column=2, row=1, padx=1, pady=1)
buttonx = ctk.CTkButton(master=root, text="*", command=multiply, width=50, height=50)
buttonx.grid(column=3, row=1, padx=1, pady=1)

button4 = ctk.CTkButton(master=root, text="4", command=number4, width=50, height=50)
button4.grid(column=0, row=2, padx=1, pady=1)
button5 = ctk.CTkButton(master=root, text="5", command=number5, width=50, height=50)
button5.grid(column=1, row=2, padx=1, pady=1)
button6 = ctk.CTkButton(master=root, text="6", command=number6, width=50, height=50)
button6.grid(column=2, row=2, padx=1, pady=1)
buttonminus = ctk.CTkButton(master=root, text="-", command=takeaway, width=50, height=50)
buttonminus.grid(column=3, row=2, padx=1, pady=1)

button1 = ctk.CTkButton(master=root, text="1", command=number1, width=50, height=50)
button1.grid(column=0, row=3, padx=1, pady=1)
button2 = ctk.CTkButton(master=root, text="2", command=number2, width=50, height=50)
button2.grid(column=1, row=3, padx=1, pady=1)
button3 = ctk.CTkButton(master=root, text="3", command=number3, width=50, height=50)
button3.grid(column=2, row=3, padx=1, pady=1)

buttondot = ctk.CTkButton(master=root, text="/", command=divide, width=50, height=50)
buttondot.grid(column=0, row=4, padx=1, pady=1)
button0 = ctk.CTkButton(master=root, text="0", command=number0, width=50, height=50)
button0.grid(column=1, row=4, padx=1, pady=1)
buttonplus = ctk.CTkButton(master=root, text="+", command=add, width=50, height=50)
buttonplus.grid(column=2, row=4, padx=1, pady=1)
buttonsolve = ctk.CTkButton(master=root, text="=", command=solve, width=50, height=104)
buttonsolve.grid(column=3, row=3, rowspan=2, sticky=tk.N, padx=1, pady=1)

root.mainloop()
