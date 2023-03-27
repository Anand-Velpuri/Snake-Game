from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

colors = ["cyan", "black", "green", "indianred"]
background_color = ""

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game by ©️Anand Velpuri")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # For random background colour generation
    for i in range(6):
        if i == 1:
            background_color = random.choice(colors)

    # Detect the collision with food
    if snake.head.distance(food) < 15:
        food.color_change()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        screen.bgcolor(background_color)
        food.color_change()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            screen.bgcolor(background_color)
            food.color_change()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
