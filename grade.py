score = input("Enter Score between 0 to 1: ")
score = float(score)

try:
    if score >= 0.9 :
        print("A")
    elif score >= 0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    elif score < 0.6 :
        print("F")
except:
    print("ERROR, score is out of range")
    quit()
