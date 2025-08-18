try:
     num1,num2=eval(input("Enter two numbers separated by a comma: ").split(","))
     result=num1/num2
     print("Result:", result)
except ZeroDivisionError :
    print("error:", "ZeroDivisionError not allowed.")
except SyntaxError:
    print("error:", "comma missing.")
except :
    print( "wrong input")
else:
    print("Input processed successfully.")
finally:
    print("Execution completed.")