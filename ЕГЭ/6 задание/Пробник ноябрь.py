from turtle import *


tracer(0)
screensize(2000, 2000)
m = 30
lt(90)
for i in range(6):
    fd(5 * m)
    rt(62)
pu()
lt(45)
fd(3 * m)
rt(45)
pd()
for i in range(5):
    fd(5 * m)
    rt(75)
pu()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(5, 'red')
done()
