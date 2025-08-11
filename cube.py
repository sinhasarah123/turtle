def cube (number):
    return number ** 3
def three_number(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(three_number(9))
print(three_number(4))