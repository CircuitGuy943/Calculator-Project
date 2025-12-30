import tkinter
import customtkinter
import time
import threading
import pyautogui


customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()  # create the Tk window like you normally do
root.geometry("400x240")
root.title("CustomTkinter Test")


def button_function():
    print("Button")
        
        
button = customtkinter.CTkButton(master=root,
                                 text="Start",
                                 command=button_function,
                                 hover_color="#00ffff",
                                 fg_color="blue",
                                 font=("bold", 30),
                                 width=120,
                                 height=30,
                                 border_width=1,
                                 corner_radius=10)

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


root.mainloop()

