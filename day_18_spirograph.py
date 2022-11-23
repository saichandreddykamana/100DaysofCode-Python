import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed('fastest')
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def spirograph(gap=5):
  for _ in range(int(360/gap)):
    t.pencolor(random_color())
    t.circle(50)
    t.setheading(t.heading() + gap)

spirograph(10)
