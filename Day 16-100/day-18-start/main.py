from turtle import Turtle, Screen, colormode
from random import randint, randrange

tim = Turtle()
tim.shape("turtle")
tim.color("DarkSeaGreen4")

#
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Random color for each
# 3 sides up to 10 sides


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)
#
# def draw_one_shape(number_of_sides):
#     if colormode() != 255:
#         colormode(255)
#     tim.pencolor(random_color())
#     rotate_angle = 360 / number_of_sides
#     for i in range(number_of_sides):
#         tim.forward(100)
#         tim.right(rotate_angle)
#
# def draw_shapes(first_side_count, ending_side_count):
#     current_sides = first_side_count
#     while current_sides <= ending_side_count:
#         draw_one_shape(current_sides)
#         current_sides = current_sides + 1
#
# draw_shapes(3, 10)

# tim.pensize(15)
# tim.speed("fast")
# colormode(255)
#
# for i in range(200):
#     tim.pencolor(random_color())
#     tim.right(randrange(0, 360, 90))
#     tim.forward(50)

tim.speed("fastest")
colormode(255)

def draw_spirograph(rotation):
    for i in range(int(360 / rotation)):
        tim.pencolor(random_color())
        tim.left(rotation)
        tim.circle(100)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()


