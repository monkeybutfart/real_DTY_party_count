import tkinter as tk
import random
from tkinter import ttk, messagebox


#data list
full_name = []
hired = []
amount_hired = []
recepit_number = []

#Constants
MIN_HIRED = 1
MAX_HIRED = 500
    
def vaild_amount(amount):
    #checks if its vaild or not.
    
    try:
        can_amount = int(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer (Can't inculde a decimal point).")
        return -1
    if can_amount < MIN_HIRED:
        messagebox.showerror("Error", "You can't hire less then one item")
        return -1
    elif can_amount > MAX_HIRED:
        messagebox.showerror("Error", "You can't hire more then 500 items")
        return -1







def log_data():
    #allows the GUI to allow inputs 
    name = name_entry.get().strip()
    hired = hired_entry.get().strip()
    amount = amount_hired_entry.get().strip()
    returns = returns_box.get()
    
    #Stops the amount from being -1
    vaild = vaild_amount((amount))
    if vaild == -1:
        return
                        

    #stops all Errors
    if name == "" or hired == "" or amount == "":
         messagebox.showerror("Error", "Please fill in all fields.")
         return
    elif name.isdigit():
        messagebox.showerror("Error", "Name can't be a number.")
        return
    elif hired.isdigit():
        messagebox.showerror("Error", "hired can't be a number.")
        return
    elif not amount.isdigit():
        messagebox.showerror("Error", "amount can only be a number.")
        return
    elif returns not in ["Yes", "No"]:
        messagebox.showerror("Error", "Please select Yes or No.")
        return




                                                                                                              

#GUI
root = tk.Tk()
root.title("Mini-Movie Fundrasier")
root.geometry ("350x200")

title_label = ttk.Label(root, text="Funland party Hiring Log", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = ttk. Entry(root, width= 25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Hired: "). grid(row=2, column=0, sticky="e")
hired_entry= ttk.Entry(root, width=25)
hired_entry.grid(row=2, column =1)

ttk.Label(root, text="Amount Hired: "). grid(row=3, column=0, sticky="e")
amount_hired_entry= ttk.Entry(root, width=25)
amount_hired_entry.grid(row=3, column =1)

ttk.Label(root, text= "return: "). grid(row=4, column=0, sticky="e")
returns_box = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
returns_box.grid(row=4, column=1)
returns_box.current(0)

submit_btn = ttk.Button(root, text= "Log data", command= log_data) 
submit_btn.grid(row=5, column=0, pady=10)

finish_btn = ttk.Button(root, text="Finish ",)
finish_btn.grid(row=5, column=1, pady=10)


root.mainloop()