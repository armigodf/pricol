from turtle import *

screensize(2000, 2000)
tracer(0)

m = 30
lt(90)

pd()
for i in range(9):
    rt(40)
    fd(2 * m)
pu()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'red')
done()
