total_billing_amount = int(input("Enter the total billing amount: "))   
amount_paid = int(input("Enter the amount paid: "))   

due_amount= total_billing_amount - amount_paid
if due_amount>0:
    print("Due amount is:", due_amount)
else:
    print("No due amount.")