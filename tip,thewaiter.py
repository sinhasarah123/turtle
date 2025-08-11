def total_calculation(bill_amount, tip_percentage):
    total= bill_amount + (bill_amount * tip_percentage / 100)
    total=round(total, 2)
    return total
print("please pay:", total_calculation(150, 20))