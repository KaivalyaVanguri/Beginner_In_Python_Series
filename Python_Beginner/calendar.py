def calendar(d, n):
    dictionary = {"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
    print("S  M  T  W  T  F  S")
    for i in range(1, n+1):
        if i == 1:
            print(" "*((dictionary[d])*2), end=" ")
        elif (i+dictionary[d]-1)%7 == 0:
            print()
        if (len(str(i))==2):
            print(i, end=" ")
        else:
            print(i, end="  ")
    
start_day = input("Enter day of the week: ")

no_of_days = int(input("Enter Number of days in the month: "))
calendar(start_day, no_of_days)
