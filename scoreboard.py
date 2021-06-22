from turtle import Turtle

alignment = "center"
text_font = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("White")
        self.penup()
        self.goto(0, 265)

        # self.write(f"Score board={self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("new.txt") as file:
            contents=file.read()
        self.write(f"Score={self.score} High score={contents}", align=alignment, font=text_font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("new.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.update_scoreboard()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=alignment, font=text_font)

    def track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
