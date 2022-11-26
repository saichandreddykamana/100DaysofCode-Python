import time
import random
from turtle import Turtle, Screen


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.game_speed = 0.1
        self.shapesize()
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=("Arial", 40, "normal"))

    def next_level(self):
        self.level += 1
        self.game_speed *= 0.9
        self.update()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        chance = random.randint(0, 6)
        if chance == 1:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
game_is_on = True
game_speed = 0.1

while game_is_on:
    time.sleep(scoreboard.game_speed)
    car.create_cars()
    car.move()
    screen.listen()
    screen.onkey(key='Up', fun=player.move)
    for screen_car in car.all_cars:
        if screen_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 260:
        scoreboard.next_level()
        player.reset()

    screen.update()
