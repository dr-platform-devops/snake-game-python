from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt", mode="r") as score_file:
            self.file_score = int(score_file.read())
        self.high_score = self.file_score
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(y=260, x=0)
        self.update_scoreboard()
        self.hideturtle()

    def news_core(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("score.txt", mode="w") as score_file_update:
                self.high_score = self.score
                score_file_update.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 28, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(arg=f"Score {self.score} High score: {self.high_score}", font=('Courier', 24, 'normal'), align="center", move=False)
