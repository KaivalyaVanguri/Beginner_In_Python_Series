a=int(input("starting number of closed interval"))
b=int(input("ending number of closed interval"))
print("( ",a," , ",b," )")
count = 0
for i in range (a,b+1):
  while(i==0):
    swap = i
    print(swap)
    n = 0 
    count = 0
    n = int(swap % 10)
    print(n)
    count = count + 1 
    print(count)
    swap = int(swap / 10)
    print(swap)
n = 0
swap = 0
sum = 0
while(n<=count):
  dig = i%10
  print(dig)
  i = int(i/10)
  print(i)
  sum = sum + dig**count
  print(sum)
  n = n +1
  print(n)
if swap==sum:
  print("it contains an armstrong number")
else:
  print("it doesn't contain an armstong number ")
  
