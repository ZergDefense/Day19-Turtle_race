import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
turtles = []
is_race_on = False

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setpos(-220, -130 + i * 50)
    new_turtle.speed(random.randint(10, 50))
    turtles.append(new_turtle)


if bet:
    is_race_on = True

winner = ""

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 20))
        if turtle.xcor() >= 220:
            is_race_on = False
            winner = turtle.color()


print(f"The winner is {winner[0]}.")
if winner[0] == bet:
    print("Your win!")
else:
    print("You lose!")


screen.exitonclick()
