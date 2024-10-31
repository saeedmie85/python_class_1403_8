import turtle
t = turtle.Turtle()
t.speed(-1)
c = 10
for i in range(50):
    t.fd(c)
    t.left(60)
    c += 10
