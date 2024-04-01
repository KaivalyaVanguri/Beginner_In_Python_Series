import re
sum = 0
fh = open('textFile1.txt','r')
stuff = fh.read()
for line in stuff:
       line = line.rstrip()
       y = re.findall('([0-9]+)',stuff)
n = len(y)
for i in range(0,n):
       num = int(y[i])
       sum = sum + num
print(n)     #88
print(sum)   #379838
