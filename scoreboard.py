from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.highscore == self.score
        self.score = 0
        self.update_scoreboard()


    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER. FINAL SCORE: {self.score}", align=ALIGNMENT, font=FONT)
