n = int(input("Enter a number to reverse"))
swap = n
i = 0
m = ''
s = ''
while swap != 0 :
  swap = int(swap / 10)
  i += 1 
  #counting number of digits 
swap = n
for j in range(i):
  s = str(swap % 10)
  m = m + s
  swap = swap // 10
  #chopping off number to extract digits 
print("Reverse Number is",int(m))
