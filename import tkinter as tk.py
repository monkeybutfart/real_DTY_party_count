import tkinter as tk
import random
from tkinter import ttk, messagebox

#Allows the Gui to function and stops errors.

#Constants
MAX_TICKETS = 150
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05

#Variables
ticket_count = 0
profit = 0


#Data lists
all_names = []
all_ages = []
all_ticket_costs = []
all_surcharges = []




#allows the right price to be picked with the age
def check_age(age):
    
    try:
        new_age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Please enter an integer (ie: a number which does not have a decimal part).")
        return -1
    if new_age < 12:
        messagebox.showerror("Error", "Please enter an integer that is more than (or equal to) 12")
        return -1
    elif new_age > 122:
        messagebox.showerror("Error", "Please enter an integer that is less than 122")
        return -1
    elif new_age < 16:
        return CHILD_PRICE
    elif new_age < 65:
        return ADULT_PRICE
    else:
        return SENIOR_PRICE
    
def submit_ticket():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    payment_method = pay_method_box.get()
    global ticket_count

   
    #stops from summitinfg anything that is blank
    if name == "" or age == "":
         messagebox.showerror("Error", "Please fill in all fields.")
         return
    elif name.isdigit():
        messagebox.showerror("Error", "Name cannot be a number.")
        return
    elif not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return
    #insures that it is impossible to break the code on the Payment method
    elif payment_method not in ["Cash", "Credit"]:
        messagebox.showerror("Error", "Please select a valid payment method.")
        return
    price = (check_age(age))
    #stops the final price from being $-1
    if price == -1:
        return
     
     
     #final payment if credit is picked.   
    elif payment_method == "Credit":
        surcharge = price * CREDIT_SURCHARGE
        total_price = price + surcharge
        
        print(f"Name: {name}, Age: {age}, Payment Method: {payment_method}")
        messagebox.showinfo(f"Ticket Submitted", f"Name: {name}\nAge: {age}\nPayment Method: {payment_method}\nTicket Price: ${(total_price):.2f}")
        all_names.append(name)
        all_ticket_costs.append(total_price)
        all_ages.append(age)
        all_surcharges.append(surcharge)
        ticket_count += 1
        if ticket_count == MAX_TICKETS:
            messagebox.showinfo("Sold Out", "All tickets have been sold.")
            submit_btn.config(state="disabled")
            return
       
    
    else: #final payment for cash
        print(f"Name: {name}, Age: {age}, Payment Method: {payment_method}")
        messagebox.showinfo(f"Ticket Submitted", f"Name: {name}\nAge: {age}\nPayment Method: {payment_method}\nTicket Price: ${(price):.2f}")
        all_names.append(name)
        all_ticket_costs.append(price)
        all_ages.append(age)
        all_surcharges.append(0)
        ticket_count += 1
        if ticket_count == MAX_TICKETS:
            messagebox.showinfo("Sold Out", "All tickets have been sold.")
            submit_btn.config(state="disabled") #stops the user from sumitting more tickets then needed
            return
       


def save_data(winner):
    total_profit = 0

    with open("attendee_details.txt", "w") as file:

        file.write("Attendee Details\n")
        file.write("====================\n\n")
        file.write(f"Lucky Winner: {winner}\n\n")
        #writes the nesscary data in the text file
        for i in range(len(all_names)):
            file.write(f"Name: {all_names[i]}\n")
            file.write(f"Age: {all_ages[i]}\n")
            file.write(f"Cost: ${all_ticket_costs[i]:.2f}\n")
            file.write(f"Surcharge: ${all_surcharges[i]:.2f}\n")
            #caulates the profit per ticket
            profit = all_ticket_costs[i] - all_surcharges[i] - 5
            total_profit += profit

            file.write(f"Profit: ${profit:.2f}\n\n")
        #adds up the total profit
        file.write(f"Overall Profit: ${total_profit:.2f}\n")

    messagebox.showinfo("Saved", "Data saved to attendee_details.txt")

#picks the  random  winner and closes the program
def finish_program():
    
    if len(all_names) > 0:
        winner = random.choice(all_names)
        messagebox.showinfo("Lucky Winner", f"{winner} wins the prize!")
        save_data(winner)
    root.quit()  


#GUI
root = tk.Tk()
root.title("Mini-Movie Fundrasier")
root.geometry ("300x300")

title_label = ttk.Label(root, text="Mini-Movie Fundraiser", font=("Verdana", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = ttk. Entry(root, width= 25)
name_entry.grid(row=1, column=1)

ttk.Label(root, text="Age: "). grid(row=2, column=0, sticky="e")
age_entry= ttk.Entry(root, width=25)
age_entry.grid(row=2, column =1)

ttk.Label(root, text="Credit Card fees(5%)"). grid(row=4, column =1)
ttk.Label(root, text= "Payment method: "). grid(row=3, column=0, sticky="e")
pay_method_box = ttk.Combobox(root, values = ["Cash", "Credit"], state = "readonly")
pay_method_box.grid(row=3, column=1)
pay_method_box.current(0)

submit_btn = ttk.Button(root, text= "Submit Ticket", command= submit_ticket) 
submit_btn.grid(row=5, column=0, pady=10)

finish_btn = ttk.Button(root, text="Finish Early", command=finish_program)
finish_btn.grid(row=5, column=1, pady=10)


root.mainloop()