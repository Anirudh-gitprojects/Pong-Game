from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.updatescore()


    def updatescore(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align='center',font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align='center',font=("Courier",80,"normal"))
        self.goto(0, 220)
        self.write("-", align='center', font=("Courier", 40, "normal"))
        self.goto(0, 180)
        self.write("Score", align='center', font=("Courier", 20, "normal"))

    def l_point(self):
        self.l_score+=1
        self.updatescore()
    def r_point(self):
        self.r_score+=1
        self.updatescore()

    def game_over(self):
        if self.l_score==5:
            self.clear()
            self.goto(0.0)
            self.write("Game Over\n Player 1 Wins", align='center',font=("Courier",20,"normal"))
        elif self.r_score==5:
            self.clear()
            self.goto(0.0)
            self.write("Game Over\n Player 1 Wins", align='center', font=("Courier", 20, "normal"))