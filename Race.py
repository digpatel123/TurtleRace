import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(title="Make the bet", prompt="Which turtle do you think will win this race? Enter the "
                                                           "color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_race_on = False

pos = 150
for t in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[t])
    tim.goto(x=-230, y=pos)
    pos -= 60
    turtles.append(tim)

if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won. The {winning_color} turtle has won the race.")
            else:
                print(f"You've lost. The {winning_color} turtle has won the race.")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
screen.exitonclick()


