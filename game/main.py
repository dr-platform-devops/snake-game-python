from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.update()

playing = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
threshold = 280

scoreboard = Scoreboard()

while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.clear()
        scoreboard.news_core()

    if snake.head.xcor() > threshold or snake.head.xcor() < -threshold or snake.head.ycor() < -threshold or snake.head.ycor() > threshold:
        scoreboard.game_over()
        playing = False

    for segments in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segments) < 10:
            playing = False
            scoreboard.game_over()

print(f"The game ended, your score is {scoreboard.score}")

screen.exitonclick()
