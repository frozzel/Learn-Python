import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(300, 300)
        self.all_cars = []
        self.top_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 12)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 0)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def create_car2(self):
            random_chance = random.randint(1, 12)
            if random_chance == 1:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                random_y = random.randint(0, 250)
                new_car.goto(-300, random_y)
                self.top_cars.append(new_car)
                
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def move_cars2(self):
        for car in self.top_cars:
            car.fd(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
