import turtle
t = turtle.Turtle()
t.speed(-1)
c = 10

for i in range(360):
    if i >= 90:
        t.fd(200)
        t.bk(200)
    t.lt(1)

