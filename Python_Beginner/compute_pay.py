
def computepay(h,r):
    if(h<=40.0):
        grpy=h*r
        p = grpy
    else:
        grpy = (h-40)*1.5*r + 40*r
        p = grpy
    return grpy
hrs = input("Enter Hours:")
rat = input("enter rate per hour:")
h = float(hrs)
r = float(rat)
p = computepay(h,r)
print("Pay",p)
