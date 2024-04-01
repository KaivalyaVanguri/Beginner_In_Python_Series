name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
counts, j  = 0, 0
for line in handle:
    line = handle.readline() #print(line)
    wds = line.split() #print(wds)
    if 'From' in wds:
        for c in wds: #print(c)
            c = wds[5].split(':') #print(c)
            time.append(c[0])
            time.sort() #print(time)
            s = set(time) #print(s)
            tim = list(s)
            tim.sort() #print(tim)
            n = len(tim)
            m = len(time) #print(time,tim)
for i in tim:
    counts = time.count(i)//7
    print(tim[j],counts)
    j +=1
 
