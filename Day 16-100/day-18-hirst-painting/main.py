from turtle import Turtle, Screen, colormode
import colorgram
import random

colors = colorgram.extract('f8fa89f20a21517430115f77166a9570.jpg', 10)

tim = Turtle()
colormode(255)
tim.penup()
tim.speed("fastest")
tim.hideturtle()

def draw_hirst(width, height, dot_size):
    new_home_x = -300
    new_home_y = 300
    tim.setpos(new_home_x, new_home_y)
    for y in range (height):
        for x in range(width):
            color = random.choice(colors).rgb
            tim.dot(dot_size, color.r, color.g, color.b)
            tim.forward(dot_size + 50)
        tim.setpos(new_home_x, new_home_y-((y + 1) * (dot_size + 50)))


draw_hirst(10, 10, 20)

screen = Screen()
screen.exitonclick()