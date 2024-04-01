n = int(input("Enter a number for counting digits "))
swap = n
count = 0
#increment variable
while swap != 0 :
  swap = int(swap / 10)
  count += 1 
swap = n 
if swap == 0:
  count = 1
#number of digits for zero is zero
print("Number of digits in this number is ",count)
