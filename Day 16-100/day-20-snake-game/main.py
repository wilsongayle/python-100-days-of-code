from turtle import Turtle, Screen, onkey, clearscreen, stamp
from random import randrange
from time import sleep

def play_worm(speed):
    worm = Turtle("square", visible=False)
    current_score_text = Turtle(visible=False)
    food = Turtle("square", visible=False)

    worm_body = []
    worm_body_coordinates = []
    current_score = 0
    game_over = False

    def build_worm(length):
        worm.speed("fastest")
        worm.penup()
        worm_body.append(worm.stamp())
        worm_body_coordinates.append(worm.pos())
        for i in range(length):
            worm.forward(20)
            worm_body.append(worm.stamp())
            worm_body_coordinates.append(worm.pos())

    def update_score():
        current_score_text.clear()
        current_score_text.write(current_score, align="center", font=("Courier", 16, "bold"))

    def add_score():
        score_text = Turtle(visible=False)
        score_text.speed("fastest")
        score_text.penup()
        score_text.setpos(-30, 370)
        score_text.write("Score:", align="center", font=("Courier", 16, "bold"))
        current_score_text.speed("fastest")
        current_score_text.penup()
        current_score_text.setpos(25, 370)
        update_score()

    def move_worm():
        worm.forward(20)
        worm_body.append(worm.stamp())
        worm_position = worm.pos()
        worm_x = round(worm_position[0], 0)
        worm_y = round(worm_position[1], 0)

        if did_hit_wall(worm_x, worm_y) or did_hit_self(worm_x, worm_y):
            end_game()

        if did_eat_food(worm_x, worm_y):
            move_food()
            nonlocal current_score
            current_score += 1
            update_score()
        else:
            worm_body_coordinates.append(worm_position)
            tail = worm_body.pop(0)
            worm.clearstamp(tail)
            worm_body_coordinates.pop(0)

    def move_right():
        worm.setheading(0)
        # move_worm()

    def move_down():
        worm.setheading(270)
        # move_worm()

    def move_left():
        worm.setheading(180)
        # move_worm()

    def move_up():
        worm.setheading(90)
        # move_worm()

    def add_food():
        food.color("red")
        food.speed("fast")
        food.shapesize(0.5)
        food.penup()
        move_food()

    def move_food():
        food.hideturtle()
        food.setpos(randrange(-360, 360, 20), randrange(-360, 360, 20))
        food.showturtle()

    def did_eat_food(worm_x, worm_y):
        food_position = food.pos()
        food_x = round(food_position[0], 0)
        food_y = round(food_position[1], 0)
        if worm_x == food_x and worm_y == food_y:
            return True
        else:
            return False

    def did_hit_wall(worm_x, worm_y):
        print('hit wall')
        if worm_x >= 400 or worm_x <= -400 or worm_y >= 400 or worm_y <= -400:
            return True
        else:
            return False

    def did_hit_self(worm_x, worm_y):
        print(f"head: {worm_x}, {worm_y}")
        for segment in worm_body_coordinates:
            segment_x = round(segment[0], 0)
            segment_y = round(segment[1], 0)
            print(segment_x, segment_y)
            if segment_x == worm_x and segment_y == worm_y:
                print('hit self')
                return True
        return False

    def end_game():
        nonlocal game_over
        game_over = True
        current_score_text.home()
        current_score_text.pencolor("red")
        current_score_text.write("GAME OVER", align="center", font=("Courier", 16, "bold"))

    build_worm(8)
    add_score()
    add_food()

    onkey(move_right, 'Right')
    onkey(move_left, 'Left')
    onkey(move_up, 'Up')
    onkey(move_down, 'Down')

    while not game_over:
        print(game_over)
        move_worm()
        sleep(speed)

screen = Screen()
screen.setup(width=1000, height=1000)
screen.listen()

play_worm(0.05)

screen.exitonclick()

