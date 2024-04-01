print("In number theory, a narcissistic number in a given number base b\nis a number that is the sum of its own digits\neach raised to the power of the number of digits - armstrong number")
num = int(input('please enter a number'))
swap = num
n = 0
count = 0
while (swap > 0):
	n = int(swap % 10) #print(n)
	count = count + 1 #print(count)
	swap = int(swap / 10) #print(swap)
swap = num #print(count)
n = 0
sum = 0
while (n <= count):
	dig = num % 10 #print(dig)
	num = int(num / 10) #print(num)
	sum = sum + dig**count #print(sum)
	n = n + 1 #print(n)
if swap == sum:
	print("it is an armstrong number")
else:
	print("it is not an armstong number ")