x1 = int(input("큰 원의 중심좌표 x1 :"))
y1 = int(input("큰 원의 중심좌표 y1 :"))
r1 = int(input(" 큰원의 반지름 :"))
x2 = int(input(" 작은 원의 중심좌표 x2 :"))
y2 = int(input("작은 원의 중심좌표 y2 :"))
r2 = int(input("작은 원의 반지름 :"))

import turtle
t = turtle.Turtle()
t.shape('turtle')

t.circle(r1)
t.circle(r2)

if r1 > r2 :
         t. write ("두번째 원이 첫번째 원 안에 있습니다.")
else :
         t. write ("첫번째 원이 두번째 원 안에 있습니다.")
