from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as open_txt:
            self.high_score = int(open_txt.read())
        self.hideturtle()
        self.goto(0, 285)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as txt_open:
                self.high_score = self.score
                txt_open.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
