mat = float(input('please enter your marks\nMathematics : '))
phy = float(input("physics :"))
che = float(input("Chemistry :"))
com = float(input("Computers :"))
eng = float(input("English :"))
avg = (mat+ phy+ che+ com + eng)/ 5
print("Average of {0}, {1}, {2},{3},{4}, is {5}".format(mat,phy,che,com,eng,avg))
if(avg<=25):
    print("Grade : F")
elif(avg >25 and avg<=45):
    print("Grade : E")
elif(avg >45 and avg<=50):
    print("Grade : D")
elif(avg<=60 and avg>50):
    print("Grade : C")
elif(avg<=80 and avg>60):
    print("Grade : B")
else:
    print("Grade : A")
