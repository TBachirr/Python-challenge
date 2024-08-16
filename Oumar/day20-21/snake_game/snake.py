import turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head =self.segment[0]
        
    def create_snake(self):
        for i in STARTING_POS: 
            self.add_segment(i)
            
    def extend(self):
        self.add_segment(self.segment[-1].position())
        
    def add_segment(self,pos):
        s= turtle.Turtle("square")
        s.penup()
        s.color("white")
        s.goto(pos)
        self.segment.append(s)
        
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            x = self.segment[seg-1].xcor()
            y = self.segment[seg-1].ycor()
            self.segment[seg].goto(x,y)
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
