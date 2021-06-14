print("Enter a number")
num = input()
i = 1
count = 0
if (int(num) == i):
	print("neither a prime nor composite number")
while (i <= int(num)):
	if (int(num) % i == 0):
		count = count + 1
	i = i + 1
if (count <= 2 and count != 1):
	print("number is prime")
elif (count > 2):
	print("number is composite")
