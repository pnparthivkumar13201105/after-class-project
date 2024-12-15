def calculate_due_amount():
    total_bill = float(input("Enter the total bill amount: "))
    
    amount_paid = float(input("Enter the amount paid by the customer: "))
    
    if amount_paid < total_bill:
        due_amount = total_bill - amount_paid
        print(f"The due amount is: ₹{due_amount:.2f}")
    elif amount_paid > total_bill:
        change = amount_paid - total_bill
        print(f"Change to be returned to the customer is: ₹{change:.2f}")
    else:
        print("The bill is fully paid. No due amount.")

calculate_due_amount()
