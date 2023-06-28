from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def move_turtle(key):
#     if key is "w":
#         move_forwards()
#     elif key is "s":
#         move_backwards()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def turn_counter_clockwise():
    tim.seth(tim.heading() + 10)


def turn_clockwise():
    tim.seth(tim.heading() - 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()


screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_counter_clockwise, "a")
screen.onkeypress(turn_clockwise, "d")
screen.onkeypress(clear_screen, "c")

screen.exitonclick()
