import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.shape('turtle')

# using tuples for colors:
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]


def draw_hirst(image_size):
    tim.hideturtle()
    tim.penup()
    x = -300
    y = -300
    tim.goto(x, y)
    for _ in range(image_size):
        for _ in range(image_size):
            tim.pendown()
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)
        y += 50
        tim.goto(x, y)

# put a value as argument to set a size of picture square in function below:
draw_hirst(5)
screen = Screen()
screen.exitonclick()
