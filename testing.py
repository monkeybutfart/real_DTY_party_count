    

print(f"Name: {name}, Hired: {hired}, Amount: {amount}")
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