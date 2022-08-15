import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from playsound import playsound

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.addshape("eran.gif")
screen.addshape("chair1.gif")
screen.addshape("chair2.gif")
screen.addshape("chair3.gif")
screen.addshape("chair4.gif")

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
    if scoreboard.score < 2:
        time.sleep(0.1)
    if 2 <= scoreboard.score < 4:
        time.sleep(0.09)
    if 4 <= scoreboard.score < 6:
        time.sleep(0.08)
    if 6 <= scoreboard.score < 8:
        time.sleep(0.07)
    if 8 <= scoreboard.score < 10:
        time.sleep(0.06)
    if 10 <= scoreboard.score < 12:
        time.sleep(0.05)
    if 12 <= scoreboard.score < 14:
        time.sleep(0.04)
    if 14 <= scoreboard.score < 16:
        time.sleep(0.03)
    if scoreboard.score >= 16:
        time.sleep(0.02)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 40:
        playsound('sound.mp3', block=False)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
