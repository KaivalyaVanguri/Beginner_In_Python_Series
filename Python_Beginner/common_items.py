l = int(input("Enter the length of the lists "))
l1  = list()
l2 = list()
count = 0
for i in range(0,l):
  n = input("Enter an element of list 1 ")
  l1.append(n)
  l1.sort() 
print(l1)
for i in range(0,l):
  m = input("Enter an element of list 2 ")
  l2.append(m) 
  l2.sort()
print(l2)
k1 = set(l1)
k2 = set(l2)
for n in k1:
  for m in k2:
    if m == n:
      count += 1
      print("Common elements",m)
print("Number of elements common",count)
if count == 0:
  print("No elements are common")
