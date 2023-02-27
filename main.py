from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()


def move_forward():
    tt.forward(20)


def move_back():
    tt.backward(20)


def turn_right():
    tt.right(5)


def turn_left():
    tt.left(5)


def clear():
    tt.clear()
    tt.penup()
    tt.home()
    tt.penup()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
