from turtle import *

screensize(3000, 3000)
tracer(0)
m = 30

lt(90)
for i in range(4):
    fd(6 * m)
    rt(90)
pu()
rt(45)
fd(2 * m)
pd()
for k in range(4):
    fd(6 * m)
    rt(90)
pu()

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * m, y * m)
        dot(5, 'red')
done()
