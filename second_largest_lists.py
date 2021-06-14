lis1 = []
l = int(input("Enter the length of the list ")) 
for i in range(0,l):
  n = int(input("Enter an element of list "))
  lis1.append(n)
  lis1.sort()
print(lis1)
second_largest = lis1[l-2]
print('Second largest number is',second_largest)
