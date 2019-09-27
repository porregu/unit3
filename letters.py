import turtle

def goto(x, y):  # this function makes mobe the pen to a coordenate without showing the line
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def m():
    turtle.left(90)
    turtle.fd(50)
    turtle.right(135)
    turtle.fd(25)
    turtle.left(100)
    turtle.fd(25)
    turtle.left(220)
    turtle.fd(50)


def i():
    turtle.left(180)
    turtle.fd(50)



def s():
    turtle.right(45)
    turtle.fd(30)
    turtle.left(120)
    turtle.fd(30)
    turtle.right(120)
    turtle.fd(30)

def p():
    turtle.right(90)
    turtle.fd(50)
    turtle.right(120)
    turtle.fd(20)
    turtle.right(45)
    turtle.fd(20)
def main():
    m()
    goto(-200,0)
    i()
    goto(-150,0)
    s()
    goto(-125,0)
    s()
    goto(-100,0)
    i()
    goto(-75,0)

turtle.exitonclick()