from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        # Need to have make_turtles here so that when we create a new snake object
        # it creates the initial 3 and has them move correctly.
        self.make_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        t = Turtle("square")
        t.color("red")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def make_snake(self):
        """This function creates turtles."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        """This function makes the turtles move."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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
