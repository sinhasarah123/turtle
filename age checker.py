try:
    age = int(input("Enter your age: "))
    if age > 0 and age <= 120:
        print("Valid age entered.")
    elif age < 0:
        print("Invalid age: Age cannot be negative.")
    elif age > 120:
        print("Invalid age: Age is unrealistically high.")
except ValueError:
    print("Invalid input: Please enter a valid integer for age.")