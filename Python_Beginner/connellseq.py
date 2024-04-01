n = 10
k = 1
j = 1
a = []
for i in range(1,n//2):
  while(j<=i):
    if k%2 != i%2:
      k+=1
    a += [k]
    j+=1
    k += 1
  j = 1
print(a[n])
