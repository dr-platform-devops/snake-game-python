from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(y=260, x=0)
        self.write(arg=f"Score {self.score}", font=('Courier', 24, 'normal'),  align="center", move=False)
        self.hideturtle()

    def news_core(self):
        self.clear()
        self.score += 1
        self.color("white")
        self.write(arg=f"Score {self.score}", font=('Courier', 24, 'normal'),  align="center", move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 28, "normal"))
