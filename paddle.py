from turtle import Turtle
# creating self. and making it to move the border of the screen from the beginning
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    # function that makes paddle to go up once user presses the button up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # function that makes paddle to go down once user presses the button down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
