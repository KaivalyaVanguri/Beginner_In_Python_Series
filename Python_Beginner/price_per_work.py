hr = input('Enter Hours:')
h = float(hr)
rt = input('Enter rate per hour')
r = float(rt)
if h<=40:
    m = r
    grspay = h*m
    print(grspay)
else:
    m = r*1.5
    grspay = (h-40)*m + (40*r)
    print(grspay)
