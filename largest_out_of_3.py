largest = None
i = 0
while(i<3):
  n = int(input("enter a number"))
  i += 1
  if(largest==None):
    largest = n
  elif(n>largest):
    largest = n
print('Largest Number',largest)
