from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

no_collision = True

while 290 > snake.head.xcor() > -300 and 290 > snake.head.ycor() > -290 and no_collision:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            no_collision = False
            score_board.reset()

score_board.reset()
score_board.game_over()

screen.exitonclick()
