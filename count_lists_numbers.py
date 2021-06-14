lis1 = []
count = 0
l = int(input("Enter the length of the list ")) 
for i in range(0,l):
  s = input("Enter words of list ")
  lis1.append(s)
  lis1.sort() 
for j in lis1:
  b = j.strip()
  a = list(b)
  k = len(a)
  if k >= 2 and a[k-1] == a[0] :
    print(j)
    count += 1
print('Number of words starting and ending with same letter and having more than two characters',count)
