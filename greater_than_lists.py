l = int(input("Enter the length of the list "))
l1  = list()
for i in range(0,l):
  n = int(input("Enter a numerical element of list "))
  l1.append(n)
n = int(input("Enter a random number "))
for m in l1 :
  if m > n:
    print("Element greater than random number",m)
