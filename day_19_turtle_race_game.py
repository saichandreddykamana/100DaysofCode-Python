from turtle import Turtle, Screen
import random


def game_setup():
    game_screen, predicted_winner = screen_setup()
    actual_winner = ''
    players = turtle_setup()
    reached = False
    while not reached:
        winner = [player.color()[0] for player in players if player.position()[0] >= 400]
        if len(winner) > 0:
            reached = True
            actual_winner = winner[0]
        else:
            player = random.choice(players)
            player.forward(10)

    game_screen.exitonclick()
    return predicted_winner, actual_winner


def player_setup(color, size, x_position, y_position):
    """ This function creates turtle players for this game."""
    turtle = Turtle()
    turtle.penup()
    turtle.shape('turtle')
    turtle.speed('fast')
    turtle.shapesize(size)
    turtle.color(color)
    turtle.setposition(x_position, y_position)
    return turtle


def turtle_setup():
    player_1 = player_setup('green', 2, -400, 0)
    player_2 = player_setup('red', 2, -400, 50)
    player_3 = player_setup('blue', 2, -400, 100)
    player_4 = player_setup('brown', 2, -400, -50)
    player_5 = player_setup('black', 2, -400, -100)
    return [player_1, player_2, player_3, player_4, player_5]


def screen_setup():
    screen = Screen()
    predicted_winner = screen.textinput('Guess the turtle color',
                                        'Enter the color of the turtle that win the race.(green, red, blue, black and '
                                        'brown) '
                                        )
    screen.setup(width=800, height=500)
    return screen, predicted_winner


def race_game():
    predicted_winner, actual_winner = game_setup()
    if predicted_winner.lower() == actual_winner.lower():
        print(f"You win. Game winner is {actual_winner}.")
    else:
        print(f"You lose. Game winner is {actual_winner}.")


race_game()
