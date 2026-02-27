import turtle

# Membuat turtle
t = turtle.Turtle()
t.speed(3)

# Fungsi Persegi Panjang (Merah)
def persegi_panjang(x, y, panjang, lebar):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(panjang)
        t.left(90)
        t.forward(lebar)
        t.left(90)
    t.end_fill()

# Fungsi Segitiga (Kuning)
def segitiga(x, y, sisi):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for i in range(3):
        t.forward(sisi)
        t.left(120)
    t.end_fill()

# Fungsi Trapesium (Hijau)
def trapesium(x, y, atas, bawah, tinggi):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.forward(bawah)
    t.left(120)
    t.forward(tinggi)
    t.left(60)
    t.forward(atas)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.end_fill()

# Fungsi Jajar Genjang (Biru)
def jajar_genjang(x, y, alas, sisi):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.forward(alas)
    t.left(60)
    t.forward(sisi)
    t.left(120)
    t.forward(alas)
    t.left(60)
    t.forward(sisi)
    t.left(120)
    t.end_fill()

# Fungsi Segilima (Ungu)
def segilima(x, y, sisi):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("purple")
    t.begin_fill()
    for i in range(5):
        t.forward(sisi)
        t.left(72)
    t.end_fill()

# Memanggil fungsi
persegi_panjang(-300, 100, 150, 80)
segitiga(-50, 100, 100)
trapesium(150, 100, 80, 150, 70)
jajar_genjang(-200, -100, 120, 80)
segilima(100, -100, 80)

turtle.done()