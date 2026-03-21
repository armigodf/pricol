from turtle import *

tracer(0)
screensize(3000, 3000)
m = 30

lt(90)

pd()
for i in range(12):
    fd(2 * m)
    rt(50)
    fd(1 * m)
    rt(-20)

pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'red')
done()
