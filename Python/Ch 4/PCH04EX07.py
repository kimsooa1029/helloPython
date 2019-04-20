c1 = input("색상 #1을 입력하시오")
c2 = input("색상 #2을 입력하시오")
c3 = input("색상 #3을 입력하시오")

import turtle
t = turtle.Turtle()
t.shape('turtle')

c_list  = [c1, c2, c3]

t. fillcolor(c_list[0])
t. begin_fill()
t. circle(50)
t. end_fill()
t. up()
t. goto (100, 0)
t. down()


t. fillcolor(c_list[1])
t. begin_fill()
t. circle(50)
t. end_fill()
t. up()
t. goto (200, 0)
t. down()

t. fillcolor(c_list[2])
t. begin_fill()
t. circle(50)
t. end_fill()
