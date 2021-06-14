l = int(input("Enter the length of the list "))
l1  = list()
l3 = list()
l4 = list()
for i in range(0,l):
  n = input("Enter an element of list ")
  l1.append(n) 
print("List you have entered",l1)
n = int(input("Enter an index to split "))
for i in range(len(l1)):
  if i < n:
    l2 = l1.copy() 
    p = l2.pop(i)
    l3.append(p)
  i += 1
for i in range(len(l1)):
  if i >= n:
    l2 = l1.copy() 
    p = l2.pop(i) 
    l4.append(p)
  i += 1
print("List before index",l3)
print("List after index",l4)
