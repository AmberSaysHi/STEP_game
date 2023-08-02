from turtle import *


colors = ["red", "coral", "orangered", "yellow", "greenyellow", "limegreen", "lime", "mediumspringgreen", "aquamarine", "cyan", "darkturquoise", "deepskyblue", "royalblue", "blue", "blueviolet", "purple", "orchid", "deeppink", "pink"]

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
    left(60)
    distance += 1