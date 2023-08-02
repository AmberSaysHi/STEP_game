from turtle import *


colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

speed(0)
i = 0
distance = 1
pensize(5)

while True:
    if i < len(colors) - 1:
        i += 1
    else:
        i = 0

    pencolor(colors[i])
    forward(distance)
    left(72)
    distance += 1