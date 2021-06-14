import math
#importing math function
a = int(input("please enter x^2 numerical coefficient: "))
b = int(input("please enter x numerical coefficient: "))
c = int(input("please enter x^0 numerical coefficient: "))
d = b*b - 4*a*c
sqroot = math.sqrt(d)
#using math function
root1 = (-b + sqroot)/(2*a)
root2 = (-b - sqroot)/(2*a)
print("solution to the quadratic equation \n{}x^2 +{}x +{}".format(a,b,c)," is ",root1,root2)
