# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count += 1
        sl = str(line)
        pos = sl.find(':')
        num = float(sl[pos+1:])
        avg += num
        if line.endswith('\n'):
            line = line.rstrip()
            #print(line)
        continue
avg = avg / count
#print(count)
print("Average spam confidence:",avg)
