from turtle import *
from math import *

# tracer(0)
#
# k = 30
#
# rt(90)
# for i in range(4):
#     fd(4 * sqrt(5) * k)
#     rt(150)
#     fd(4 * sqrt(5) * k)
#     rt(300)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(4, 'blue')
# done()


# tracer(0)
# k = 30
#
# rt(180)
# fd(2 * k)
# rt(90)
# fd(40 * k)
# rt(90)
# fd(2 * k)
# for i in range(4):
#     circle(5, 180)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(4, 'blue')
# done()


# screensize(3000, 3000)
# tracer(0)
# m = 30
#
# lt(90)
# pd()
# fd(5 * m)
# rt(120)
# fd(10 * m)
# rt(150)
# fd(3 * m)
# for i in range(2):
#     fd(10 * m)
#     rt(90)
#     fd(3 * m)
#     rt(90)
#
# pu()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x * m, y * m)
#         dot(5, 'red')
#
# done()


screensize(3000, 3000)
tracer(0)
m = 30

lt(90)

for i in range(7):
    fd(3 * m)
    rt(66)
    fd(1 * m)

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, 'red')

done()
