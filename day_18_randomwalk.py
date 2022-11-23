import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.pensize(5)

########### Challenge 4 - Random Walk ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [90, 270, 0]
sides = ['left', 'right']
actions = ['forward', 'backward']
def random_walk():
  for i in range(0, 100):
    tim.pencolor(colours[random.randint(0, len(colours) - 1)])
    tim_side = sides[random.randint(0, len(sides) - 1)]
    if tim_side == 'forward':
      tim.forward(10)
    else:
      tim.backward(10)
    tim_action = actions[random.randint(0, len(actions) - 1)]
    if tim_action == 'left':
      tim.left(angles[random.randint(0, len(angles) - 1)])
    else:
      tim.right(angles[random.randint(0, len(angles) - 1)])

random_walk()
