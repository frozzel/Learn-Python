from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score_count = 0
        self.penup()
        self.hideturtle()
        self.color("aqua")
        self.goto(0,270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_count} High Score: {self.high_score}", align="center", font=("Robo", 24, "normal"))
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Robo", 40, "normal"))
        
    def increase_score(self):
        self.score_count += 1
        self.update_score()
        
    def reset(self):
        if self.score_count > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score_count
                file.write(f"{self.high_score}")
        self.score_count =0
        self.update_score()
        
        