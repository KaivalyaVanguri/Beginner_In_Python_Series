import math
#importing math function
a = float(input("please enter side 1 of the triangle: "))
b = float(input("please enter side 2 of the triangle: "))
c = float(input("please enter side 3 of the triangle: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#using math.sqrt function
print("area of triangle is ",area)
