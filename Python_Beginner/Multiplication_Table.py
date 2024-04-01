num=0
n=0
print("enter a number for printing a multiplication table")
num = input()
print("enter an index")
n = input()
i = 0
while (i<=int(n)): 
    #printing multiplication table
    prod = (int(num)*i)
    print("{0}*{1}={2}\n".format(num,i,prod))
    i = i + 1
