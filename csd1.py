a1 = input("1st binary number: ")
b1 = input("2nd binary number: ")
m = max(len(a1), len(b1))
s = [0]*m
#t = 0
d = {'0':'0', '1': '1', '2':'10', '3':'11'}
for i in range(m-1,-1, -1):
    if i <= len(a1) and i <= len(b1):
        s[i] = d.get(str(a1[i]+b1[i]))
        print(d.get(str(a1[i]+b1[i])))
    elif i <= len(a1):
        s[i] = d.get(str(a1[i]))
    elif i <= len(b1):
        s[i] = d.get(str(b1[i]))
print(s)
print(str(s[::-1]).strip(", ").strip("[]"))
               
