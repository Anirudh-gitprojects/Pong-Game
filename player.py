from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()

    def add_player1(self,name):
        self.goto(-350,240)
        self.write(f"{name}", align='center', font=("Courier", 20, "normal"))

    def add_player2(self,name):
        self.goto(350, 240)
        self.write(f"{name}", align='center', font=("Courier", 20, "normal"))