from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle()
            new_car.pu()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.setposition(x=290, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
