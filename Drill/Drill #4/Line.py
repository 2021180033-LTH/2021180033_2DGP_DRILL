import turtle

a = 4
while(a>0):
    turtle.forward(500)
    turtle.left(90)
    a -= 1

b = 2
while(b>0):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    b -= 1
turtle.forward(20)

c = 2
while(c>0):
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    c -= 1
