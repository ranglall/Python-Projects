"""
PasswordGenTkinter.py
Author: Breanna Ranglall
Use Tkinter to create a GUI for PasswordGenerator.py
"""

import tkinter as tk

def min_length():
    try:
        # Get the integer from the entry widget
        value = int(entry.get())
        # Store the integer in a variable
        user_integer.set(value)
    except ValueError:
        # If the input is not a valid integer, handle the exception
        user_integer.set("Invalid input")

# Create the main tkinter window
win = tk.Tk()
win.title("Integer Input")

# Variable to store the user's integer input
user_integer = tk.StringVar()

# Create an entry widget to input the integer
entry = tk.Entry(win, textvariable=user_integer)
entry.grid(row=0, column=0, pady=10)

# Create a button to submit the integer
button = tk.Button(win, text="Submit", command=min_length)
button.grid(row=0, column=1, pady=10)

# Create Yes/No radio buttons in their own row
radio_value = tk.IntVar()
radio_value.set(0)  # Set an initial value

radio_yes = tk.Radiobutton(win, text="Yes", variable=radio_value, value=1)
radio_yes.grid(row=1, column=0, pady=5)

radio_no = tk.Radiobutton(win, text="No", variable=radio_value, value=0)
radio_no.grid(row=1, column=1, pady=5)

# Start the tkinter event loop
win.mainloop()



