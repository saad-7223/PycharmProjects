import turtle as t

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_seg = t.Turtle("square")
        new_seg.color("white")
        new_seg.pu()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        # this line specifies at what position should snake be extended
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[i - 1].xcor()
            new_y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_cor, new_y_cor)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
