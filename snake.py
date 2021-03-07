from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, position):
        snake_1 = Turtle("square")
        snake_1.color("white")
        snake_1.penup()
        snake_1.goto(position)
        self.snake_segments.append(snake_1)

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    def snake_move(self):
        for item in range(len(self.snake_segments) - 1, 0, -1):
            x_pos = self.snake_segments[item - 1].xcor()
            y_pos = self.snake_segments[item - 1].ycor()
            self.snake_segments[item].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

