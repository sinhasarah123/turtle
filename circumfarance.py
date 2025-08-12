def find_circumference(radius):
   return 2 * 3.14 * radius
r = float(input("Enter the radius of the circle: "))
c = find_circumference(r)
print(f"The circumference of the circle with radius {r} is: {c}")