from turtle import Turtle, Screen
import random

def etch_a_sketch():
    tim = Turtle()
    screen = Screen()

    def move_forwards():
        tim.forward(10)

    def move_backwards():
        tim.backward(10)

    def turn_left():
        tim.left(10)

    def turn_right():
        tim.right(10)

    def clear():
        tim.reset()

    screen.listen()
    screen.onkey(move_forwards, 'w')
    screen.onkey(move_backwards, 's')
    screen.onkey(turn_left, 'a')
    screen.onkey(turn_right, 'd')
    screen.onkey(clear, 'c')

    screen.exitonclick()

def turtle_race():
    race_over = False

    turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []

    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

    for index, color in enumerate(turtle_colors):
        turtle = Turtle('turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=(125-(index*50)))
        turtles.append(turtle)

    while not race_over:
        turtle = random.choice(turtles)
        turtle.forward(random.randint(10, 20))
        if turtle.xcor() > 230:
            race_over = True
            print(f"Race over, {turtle.pencolor()} wins!")
            if user_bet == turtle.pencolor():
                print("you guessed correctly!")
            else:
                print("you guessed incorrectly!")

    screen.exitonclick()

turtle_race()