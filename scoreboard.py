from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,470)
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        #self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

