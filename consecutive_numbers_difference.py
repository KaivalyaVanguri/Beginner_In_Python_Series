lis1 = []
l = int(input("Enter the length of the list ")) 
for i in range(0,l):
  try :
    n = int(input("Enter an element of list "))
    lis1.append(n)
  except:
    print("Input integers only") 
    break
for i in range(0,l) :
  if i != l-1:
    sub = lis1[i+1] - lis1[i]
    print("Difference of Consecutive Numbers",sub)
