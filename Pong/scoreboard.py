from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_count_pd1 = 0
        self.score_count_pd2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
        
            
    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.score_count_pd2}", align="center", font=("Robo", 60, "normal"))
        self.goto(100, 230)
        self.write(f"{self.score_count_pd1}", align="center", font=("Robo", 60, "normal"))  
              
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Robo", 40, "normal"))
        
    def l_point(self):
        self.score_count_pd1 += 1
        
    def r_point(self):
        self.score_count_pd2 += 1
        

