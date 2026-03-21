from turtle import *

screensize(3000, 3000)
tracer(0)
m = 30

lt(90)

for i in range(4):
    fd(8 * m)
    rt(90)

rt(45)
fd(6 * m)
rt(45)
fd(4 * m)

pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, 'red')
done()
