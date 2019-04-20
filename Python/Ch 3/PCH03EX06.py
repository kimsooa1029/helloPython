import turtle
t = turtle.Turtle()
t.shape('turtle')

x1 = int(input(" x1점"))
y1 = int(input(" y1점"))
x2 = int(input(" x2점"))
y2 = int(input(" y2점"))

t.goto(x1, y1)
t.goto(x2, y2)

result = ((x1-x2)**2+(y1-y2)**2)**0.5

t.write("직선의 길이 = "+ str(result))
