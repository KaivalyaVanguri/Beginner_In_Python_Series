import turtle
bob = turtle.Turtle()
def shapes_turt(n) :
    "This is a doc_string for circles, squares, rectangles and triangles"
    print(bob)
    try:
        bob.pd()
     if n == 's':
        for i in range(4):
            bob.lt(90)
            bob.fd(100)
     elif n == 'c':
         for i in range(360):
             bob.lt(1)
             bob.fd(1)
     elif n == 't':
         for i in range(3):
             bob.lt(60)
             bob.fd(100)
     elif n == 'r':
        for i in range(2):
            bob.lt(90)
            bob.fd(100)
            bob.lt(90)
            bob.fd(50)
    except:
        print('Please enter appropriate letter')
n = input('Enter s for square, r for rectangle, c for circle and t for triangle')
shape = shapes_turt(n)
turtle.penup()
