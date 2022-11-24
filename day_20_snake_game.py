import random
import time
from turtle import Turtle, Screen

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
FOOD_COLORS = ['RED', 'BLUE', 'YELLOW', 'PINK', 'LIGHTBLUE', 'LIGHTGREEN', 'LIGHTGRAY']
MOVE_DISTANCE = 20
RIGHT_ANGLE = 0
UP_ANGLE = 90
LEFT_ANGLE = 180
DOWN_ANGLE = 270


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shapesize(stretch_wid=600)
        self.color('white')
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=("Arial", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color(random.choice(FOOD_COLORS))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def change_food(self):
        self.color(random.choice(FOOD_COLORS))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


class Snake:
    def __init__(self):
        self.shape = 'square'
        self.color = 'white'
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.create_snake_segment(position=position)

    def increase_snake(self):
        self.create_snake_segment(self.snake[-1].position())

    def create_snake_segment(self, position):
        snake_seg = Turtle(self.shape)
        snake_seg.color(self.color)
        snake_seg.penup()
        snake_seg.goto(position)
        self.snake.append(snake_seg)

    def move_snake(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            x_cor = self.snake[segment - 1].xcor()
            y_cor = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x_cor, y_cor)
        self.snake_head.forward(MOVE_DISTANCE)
        return self.snake_head.position()

    def move_left(self):
        if self.snake_head.heading() != RIGHT_ANGLE:
            self.snake_head.setheading(LEFT_ANGLE)

    def move_right(self):
        if self.snake_head.heading() != LEFT_ANGLE:
            self.snake_head.setheading(RIGHT_ANGLE)

    def move_up(self):
        if self.snake_head.heading() != DOWN_ANGLE:
            self.snake_head.setheading(UP_ANGLE)

    def move_down(self):
        if self.snake_head.heading() != UP_ANGLE:
            self.snake_head.setheading(DOWN_ANGLE)


game_screen = Screen()
game_screen.setup(width=700, height=700)
game_screen.bgcolor('black')
game_screen.title('Snake Game')
game_screen.tracer(0)

snake = Snake()
snake_food = Food()
scoreboard = ScoreBoard()
game = True

while game:
    game_screen.update()
    time.sleep(0.05)
    current_position = snake.move_snake()
    if abs(current_position[0]) > 340 or abs(current_position[1]) > 300:
        game = False
        scoreboard.game_over()
    elif snake.snake_head.distance(snake_food) < 15:
        snake_food.change_food()
        snake.increase_snake()
        scoreboard.increase_score()

    for segment in snake.snake:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game = False
            scoreboard.game_over()
    game_screen.listen()
    game_screen.onkey(key="w", fun=snake.move_up)
    game_screen.onkey(key="s", fun=snake.move_down)
    game_screen.onkey(key="a", fun=snake.move_left)
    game_screen.onkey(key="d", fun=snake.move_right)

game_screen.exitonclick()

