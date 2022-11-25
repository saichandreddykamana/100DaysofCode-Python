import time
from turtle import Turtle, Screen
DISTANCE = 40
PADDLE_Y_LIMIT = -230
BALL_MOVE_DISTANCE = 10
WALL_BORDER = -280
BALL_EDGE = -380


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shapesize(stretch_wid=600)
        self.color('white')
        self.penup()
        self.goto(0, 250)
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


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_cor = self.y_cor = BALL_MOVE_DISTANCE

    def move(self):
        self.goto(self.xcor() + self.x_cor, self.ycor() + self.y_cor)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.x_cor = x_cor
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, 0)
        self.goto(x_cor, 0)

    def move_up(self):
        if int(self.position()[1]) < abs(PADDLE_Y_LIMIT):
            self.goto(self.x_cor, self.ycor() + DISTANCE)

    def move_down(self):
        if int(self.position()[1]) > PADDLE_Y_LIMIT:
            self.goto(self.x_cor, self.ycor() - DISTANCE)


game_screen = Screen()
game_screen.bgcolor('black')
game_screen.setup(width=800, height=600)
game_screen.title('Ping Pong')
game_screen.tracer(0)

# Paddles
left_paddle = Paddle(-370)
right_paddle = Paddle(370)

# ball
ball = Ball()

# Scoreboard
scoreboard = ScoreBoard()

game_screen.listen()
game_screen.onkey(key='Up', fun=right_paddle.move_up)
game_screen.onkey(key='Down', fun=right_paddle.move_down)
game_screen.onkey(key='w', fun=left_paddle.move_up)
game_screen.onkey(key='s', fun=left_paddle.move_down)

game = True
while game:
    time.sleep(0.04)
    game_screen.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() > abs(WALL_BORDER) or ball.ycor() < WALL_BORDER:
        ball.bounce_y()

    # Detect ball collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or\
            ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        scoreboard.increase_score()
        ball.bounce_x()
        
    if ball.xcor() > abs(BALL_EDGE) or ball.xcor() < BALL_EDGE:
        scoreboard.game_over()
        game = False
game_screen.exitonclick()
