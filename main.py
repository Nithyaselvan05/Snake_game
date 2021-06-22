from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

snake = Snake()
food = Food()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(height=600, width=600)
screen.bgcolor("black")
# turtle.shape("square")
# turtle.shapesize(1, 5)
screen.title("My snake game")
position = [(0, 0), (-20, 0), (-40, 0)]
segment = list()
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_turn()
    if snake.head.distance(food) < 15:
        scoreboard.track()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.gameover()
        # scoreboard.game_over()
        # game_on = False
    for i in snake.segment[1:]:

        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.gameover()
            # game_on = False
            # scoreboard.game_over()

screen.exitonclick()
