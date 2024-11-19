from turtle import Turtle, Screen
# Scoreboard creation

screen = Screen()
user_1 = screen.textinput("PONG...", "Player1 Name :")
user_2 = screen.textinput("PONG...", "Player2 Name :")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1 = user_1
        self.p2 = user_2
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 210)
        self.write(f"{self.p1}: {self.l_score}", False, "center", ("Courier", 20, "normal"))
        self.goto(150, 210)
        self.write(f"{self.p2}: {self.r_score}", False, "center", ("Courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
