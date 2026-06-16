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


submit_btn = ttk.Button(root, text= "Submit Ticket" ) 
submit_btn.grid(row=5, column=0, pady=10)

finish_btn = ttk.Button(root, text="Finish")
finish_btn.grid(row=5, column=1, pady=10)


root.mainloop()