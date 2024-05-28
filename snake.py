from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

NUM_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

x = 0
y = 0

segments = []

class OurSnake:
    def __init__(self):
        self.segments = []
        self.create_snake(NUM_SEGMENTS, x, y)
        self.head = self.segments[0]

    def create_snake(self, NUM_SEGMENTS, x, y):
        for index in range(0, NUM_SEGMENTS):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("brown")
            #new_segment.color(COLORS[index])
            new_segment.penup()
            new_segment.goto(x, y)
            self.segments.append(new_segment)
            x -= 20
            #print(f"33 snake.py self.segments = {self.segments}")

    def add_segment(self):
        #self.last_seg = self.segments[len(segments) -1]
        self.last_seg = self.segments[-1]
        last_new_x = self.last_seg.xcor()
        last_new_y = self.last_seg.ycor()
        self.create_snake(1, last_new_x, last_new_y)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            #time.sleep(0.1)
            self.segments[seg_num].goto(new_x, new_y)
            #screen.update()
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        #if self.head.heading() != 270.0:
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        #if self.head.heading() != 90.0:
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def turn_left(self):
        #if self.head.heading() != 0.0:
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def turn_right(self):
        #if self.head.heading() != 180.0:
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    # def clear(self):
    #     ### clear the screen ###
    #     for segment in all_segments:
    #         segment.reset()

    def segment_color(self, index):
        print(f"78 snake.py index = {index}")
        segments[index].color(colors[index])

    def get_pos(self):
        return self.head.pos()