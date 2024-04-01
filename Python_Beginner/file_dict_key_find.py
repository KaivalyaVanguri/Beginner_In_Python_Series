name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
count = 0
for line in handle:
    line = handle.readline()
    wds = line.split(' ')
    if wds[0]=='From':
        count += 1
        dic.update({wds[1]:count})
        continue
k = list(dic.keys())
v = list(dic.values())
#print(k,v)
m = max(v)
#print(m)
pos = v.index(m)
#print(pos)
key = k[pos]
print(key,pos+1)
''''equivalent code for the last print statement:
print(list(dic.keys())[list(dic.values()).index(m)])''''
