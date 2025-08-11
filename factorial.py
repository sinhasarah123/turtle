def factorial (x):
    '''this is a docstring'''
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
    print (factorial.__doc__)
    print (f"the factorial of 0 is {factorial(0)}")
    print (f"the factorial of 5 is {factorial(5)}")
    print (f"the factorial of 10 is {factorial(10)}")