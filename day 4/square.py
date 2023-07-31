import turtle

def square(): 
    size = int(input("Please enter the size here ")) 
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)



square()
turtle.done()