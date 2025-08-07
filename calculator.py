def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b
print("select operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Enter choice (a/b/c/d): ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if choice == 'a':
    print(num_1, "+", num2, "=", add_numbers(num1, num2))
elif choice == 'b':
    print(num1, "-", num2, "=", subtract_numbers(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply_numbers(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide_numbers(num1, num2))
else:
    print("Invalid input")