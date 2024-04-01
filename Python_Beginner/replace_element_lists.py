l = int(input("Enter the length of the list "))
l1  = list()
l2 = list()
count = 0
for i in range(0,l):
  n = input("Enter an element of list ")
  l1.append(n)
print(l1)
for i in range(0,l):
  m = input("Enter an element of another list for replace ")
  l2.append(m) 
#print(l2)
l3 = l2.copy()
l1[l-1] = l3.pop(l-1)
print(l1) 
