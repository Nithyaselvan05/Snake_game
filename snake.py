from turtle import Turtle

position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.snake_move()
        self.head = self.segment[0]

    def snake_move(self):
        for i in position:
            self.add_segment(i)

    def add_segment(self, position_now):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position_now)
        self.segment.append(turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def gameover(self):
        # self.head.goto(0, 0)
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.snake_move()
        self.head = self.segment[0]

    def snake_turn(self):

        for j in range(len(self.segment) - 1, 0, -1):
            cordx = self.segment[j - 1].xcor()
            cordy = self.segment[j - 1].ycor()
            self.segment[j].goto(cordx, cordy)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == 270:
            self.head.setheading(270)
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            self.head.setheading(90)
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            self.head.setheading(0)
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            self.head.setheading(180)
        else:
            self.head.setheading(0)
