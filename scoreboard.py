from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.hideturtle()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(-210, 230)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
