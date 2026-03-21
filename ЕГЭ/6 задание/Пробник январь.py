from turtle import *


tracer(0)
screensize(2000, 2000)
m = 30
lt(90)
for i in range(14):
    fd(4 * m)
    rt(60)
pu()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'green')
done()
