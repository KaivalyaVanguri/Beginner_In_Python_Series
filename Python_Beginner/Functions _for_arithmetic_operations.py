def add(x,y):
  z = x + y
  return z
def sub(x,y):
  z = x - y
  return z
def pro(x,y):
  z = x*y
  return z
def div(x,y):
  z = x/y
  return z
n = input("Addition : a \nSubtraction : s \nMultiplication : m \nDivision :d\nplease enter a letter for the respective operation") 
a = input("Enter a number")
b = input("enter another number")
try: 
  a = int(a)
  b = int(b)
  if n == 'a':
    c = add(a,b)
  elif n == 's':
    c = sub(a,b)
  elif n == 'm':
    c = pro(a,b)
  elif n == 'd':
    c = div(a,b)
  print(c)
except:
  print("Please enter numbers for operand")
if (n != 'a' and n != 's' and n!= 'm' and n != 'd'):
  print("please enter letters only for choosing operation") 
