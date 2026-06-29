import tkinter as tk
import random
from tkinter import ttk, messagebox


#data list
full_name = []
hired_yes = []
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

    return can_amount





def log_data():
    #allows the GUI to allow inputs 
    name = name_entry.get().strip()
    hired = hired_entry.get().strip()
    amount = amount_hired_entry.get().strip()
    
    
    #genrates a recepit
    recepit = random.randint(1000000000, 99999999999999999999)

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
   
    else:
        print(f"Name: {name}, Hired: {hired}, Amount: {amount}, recepit: {recepit} ")
        messagebox.showinfo(f"Info Logged", f"Name: {name}\nHired: {hired}\nAmount Hired: {amount}\nrecepit: {recepit}")
        full_name.append(name)
        hired_yes.append(hired)
        amount_hired.append(amount)
        recepit_number.append(recepit)
        returns_box["values"] = recepit_number
        return

 #saves the data to a text file     
def save_data():
    

    with open("attendee_details.txt", "w") as file:
        
        file.write("====================\n")
        file.write("Party hire\n")
        file.write("====================\n\n")
        
        for i in range(len(full_name)):
            file.write(f"Name: {full_name[i]}\n")
            file.write(f"Hired: {hired_yes[i]}\n")
            file.write(f"Amount Hired: {amount_hired[i]}\n")
            file.write(f"Recepit: {recepit_number[i]}\n\n")
            
            
    return
#allows the user to do returns       
def returns():
    taco = returns_box.get()
    
    if taco == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    recepit = int(taco)


    if recepit in recepit_number:
        index = recepit_number.index(recepit)
        del full_name[index]
        del hired_yes[index]
        del amount_hired[index]
        del recepit_number[index]
        
        
        returns_box["values"] = recepit_number
        
        messagebox.showinfo("it worky")
        returns_box.set('')
        return
    
    
       
                                                                                                              

#GUI
root = tk.Tk()
root.title("Mini-Movie Fundrasier")
root.geometry ("350x350")

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

submit_btn = ttk.Button(root, text= "Save", command=lambda:(log_data(), save_data()))
submit_btn.grid(row=5, column=1, pady=10)

title_label = ttk.Label(root, text="Returns", font=("Verdana", 18, "bold"))
title_label.grid(row=6, column=0, columnspan=2, pady=10)

ttk.Label(root, text= "Put in the recepit number: "). grid(row=7, column=0, sticky="e")
returns_box = ttk.Combobox(root, values = [], state = "readonly")
returns_box.grid(row=7, column=1)

submit_btn = ttk.Button(root, text= "remove return",command= returns)
submit_btn.grid(row=8, column=1, pady=10)

root.mainloop() 