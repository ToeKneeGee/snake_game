# written by Anthony Guba

import time
from turtle import Screen

from food import Food
from snake import OurSnake

import scoreboard
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Tony's Snake Game")
screen.tracer(0)

snake = OurSnake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
#screen.onkey(snake.clear, "c")

go = True
while go:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.head.xcor() > 490:
        print("38 game over")
        go = False
        scoreboard.game_over()
    elif snake.head.xcor() < -495:
        print("42 game over")
        go = False
        scoreboard.game_over()
    elif snake.head.ycor() > 495:
        print("46 game over")
        go = False
        scoreboard.game_over()
    elif snake.head.ycor() < -490:
        print("50 game over")
        go = False
        scoreboard.game_over()

    # detect collision with food
    #print(f"55 food = {food}")
    #print(f"56 food.pos = {food.pos()}")
    if snake.head.distance(food) < 15:
        print("yummo")
        food.refresh()
        snake.add_segment()
        scoreboard.increment_score()

    # detect collision with tail
    # game over if tail collides with any other segment

    # for num in range(1, len(snake.segments)):
    #     segment = snake.segments[num]
    #for segment in snake.segments[1:(len(snake.segments))]:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            print(f"71 {segment.pos()} {snake.head.pos()}")
            go = False
            scoreboard.game_over()

screen.exitonclick()
