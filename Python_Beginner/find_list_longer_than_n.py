lis1 = []
l = int(input("Enter the length of the lists ")) 
count = 0
for i in range(0,l):
  w = input("Enter words of list ")
  lis1.append(w)
  lis1.sort() 
n = int(input("Enter a number to check the length of words more than the given number "))
for j in lis1:
  a = list(j)
  k = len(a)
  if k > n:
    print('Words longer than given number',j)
    count += 1
print("Number of words longer than given number",count)
