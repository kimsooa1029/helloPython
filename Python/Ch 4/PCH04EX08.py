x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

import turtle
t = turtle.Turtle()
t.shape('turtle')

n_list = [x1, y1, x2, y2, x3, y3]


t.goto(n_list[0], n_list[1])


t.goto(n_list[2], n_list[3])


t.goto(n_list[4], n_list[5])
