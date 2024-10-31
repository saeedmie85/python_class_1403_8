import turtle
t = turtle.Turtle()
t.speed(-1)
c = 10

for i in range(360):
    if 90 <= i <= 180 or 270 <= i <= 360:  
        t.lt(1)
    else:
        t.fd(200)
        t.bk(200)
        t.lt(1)

