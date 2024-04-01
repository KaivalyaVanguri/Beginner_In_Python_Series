fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = fh.readline()
    words = line.split(' ')
    if words[0] == 'From':
        print(words[1])
        count += 1
        ''''words.clear() This line is unnecessary ''''

print("There were", count, "lines in the file with From as the first word")
