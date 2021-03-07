import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake_character = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake_character.up, "Up")
my_screen.onkey(snake_character.down, "Down")
my_screen.onkey(snake_character.left, "Left")
my_screen.onkey(snake_character.right, "Right")

my_screen.update()

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake_character.snake_move()

    # detect snake collides with the food
    if snake_character.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake_character.extend_snake()

    # detect snake collides with the walls
    if (snake_character.head.xcor() > 280 or snake_character.head.xcor() < -280 or
            snake_character.head.ycor() > 280 or snake_character.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False

    # detect snake collides with its body
    for segment in snake_character.snake_segments[1:]:
        if snake_character.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

my_screen.exitonclick()
