import turtle

turtle.speed(100)
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
    turtle.seth(0)
    turtle.seth(0)


def i():
    turtle.left(90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.seth(0)


def s():
    turtle.right(300)
    turtle.fd(30)
    turtle.left(120)
    turtle.fd(30)
    turtle.right(120)
    turtle.fd(30)
    turtle.seth(0)

def p():
    turtle.right(270)
    turtle.fd(50)
    turtle.right(120)
    turtle.fd(20)
    turtle.right(45)
    turtle.fd(20)
    turtle.left(270)
    turtle.fd(20)
    turtle.seth(0)


def main():
    goto(-200,0)
    m()
    goto(-150,0)
    i()
    goto(-125,0)
    s()
    goto(-100,0)
    s()
    goto(-75,0)
    i()
    goto(-50,0)
    s()
    goto(-25,0)
    s()
    goto(0,0)
    i()
    goto(25,0)
    p()
    goto(60,0)
    p()
    goto(90,0)
    i()

main()
turtle.exitonclick()