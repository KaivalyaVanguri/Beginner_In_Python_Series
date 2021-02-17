largest = None
smallest = None
while True:
        num = input("Enter a number: ")
        if num != "done" :
            try:
                n = int(num)
                if largest is None:
                    largest = n
                if smallest is None:
                    smallest = n
                if largest < n:
                    largest = n
                if smallest > n:
                    smallest = n
            except:
                print("Invalid input")
         if num == "done" :
            break

print("Maximum is",largest)
print("Minimum is",smallest)
