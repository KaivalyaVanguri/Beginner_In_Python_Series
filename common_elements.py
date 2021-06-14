#list1 = [41,12,78,9,55]
#list2 = [55,31,45,21,8]
l = int(input("Enter the length of the lists "))
l1  = list()
l2 = list()
a = False
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
  if n in k2:
      print(n)
      a = True 
if a == False :
  print("No elements are common")
else:
  print("There is atleast one common element")
