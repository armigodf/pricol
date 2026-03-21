from turtle import *

screensize(2000, 2000)
tracer(0)
m = 30


lt(90)
for i in range(9):
    fd(7 * m)
    rt(90)
    fd(42 * m)
    rt(90)
pu()

back(10 * m)
lt(90)
back(16 * m)
pd()

for j in range(9):
    fd(42 * m)
    rt(90)
    fd(16 * m)
    rt(90)

for x in range(-200, 200):
    for y in range(-200, 200):
        setpos(x * m, y * m)
        dot(5, 'red')
done()
