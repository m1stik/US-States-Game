from turtle import Turtle

class DrawMap(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
    
    def display_state(self, state, x, y):
        self.setpos(x, y)
        self.write(f"{state}", False, align="center", font=("Tahoma", 12, "normal"))

    def gameover(self):
        self.setpos(0, 0)
        self.color("green")
        self.write("You won!", False, align="center", font=("Tahoma", 20, "normal"))