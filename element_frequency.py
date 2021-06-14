lis1 = []
l = int(input("Enter the length of the list ")) 
count = 0
t = 0
for i in range(0,l):
  n = input("Enter an element of list ")
  lis1.append(n)
  lis1.sort() 
print(lis1)
lis2 = lis1.copy()
f = input("Enter an element to check its frequency ")
for n in lis1:
  for m in lis2:
    if m == n :
      if m == f:
        t += 1 
      count += 1
print("Element frequency is",t-(count-l))
if count - l == 0:
  print("No elements are common")
  print("frequency for all elements is",1)
