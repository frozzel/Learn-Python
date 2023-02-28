from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.penup()
        self.hideturtle()
        self.color("aqua")
        self.goto(0,270)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score_count}", align="center", font=("Robo", 24, "normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Robo", 40, "normal"))
        
    def increase_score(self):
        self.score_count += 1
        self.clear()
        self.update_score()
        