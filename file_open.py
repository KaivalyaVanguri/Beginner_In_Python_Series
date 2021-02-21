# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname,'r')
inp = fh.read()
for line in inp:
    if line.endswith('\n'):
       line = line.rstrip()
print(inp.upper())
