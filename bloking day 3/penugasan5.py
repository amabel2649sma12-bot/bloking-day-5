import turtle

t = turtle.Turtle()
t.speed(0)
t.width(2)

screen = turtle.Screen()
screen.bgcolor("white")

# Posisi awal
t.penup()
t.goto(0, -100)
t.pendown()

# Warna daun
t.color("darkgreen")
t.fillcolor("green")

t.begin_fill()

# Sisi kiri daun
t.left(60)
t.circle(150, 60)

# Sisi kanan daun
t.left(120)
t.circle(150, 60)

t.end_fill()

# ===== Tulang daun =====
t.penup()
t.goto(0, -100)
t.setheading(90)
t.pendown()
t.color("darkgreen")
t.forward(170)

# Garis kecil tulang daun
for i in range(5):
    t.backward(30)
    t.right(45)
    t.forward(40)
    t.backward(40)
    t.left(90)
    t.forward(40)
    t.backward(40)
    t.right(45)

t.hideturtle()
turtle.done()