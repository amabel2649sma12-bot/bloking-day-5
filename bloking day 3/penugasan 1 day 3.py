import turtle

t = turtle.Turtle()
t.speed(5)
 
# Persegi Panjang
def persegi_panjang(panjang, lebar):
    for i in range(2):
        t.forward(panjang)
        t.right(90)
        t.forward(lebar)
        t.right(90)

# Segitiga Sama Kaki
def segitiga(sisi):
    for i in range(3):
        t.forward(sisi)
        t.left(120)

# Trapesium Sama Kaki
def trapesium(atas, bawah, sisi_miring):
    t.forward(bawah)
    t.left(120)
    t.forward(sisi_miring)
    t.left(60)
    t.forward(sisi_miring)
    t.left(120)

# Jajar Genjang
def jajar_genjang(panjang, sisi):
     t.forward(panjang)
     t.left(60)
     t.forward(sisi)
     t.left(120)
     t.forward(panjang)
     t.left(60)
     t.forward(sisi)
     t.left(sisi)

# Belah Ketupat
def belah_ketupat(sisi):
    t.forward(sisi)
    t.left(60)
    t.forward(sisi)
    t.left(120)
    t.forward(sisi)
    t.left(60)
    t.forward(sisi)
    t.left(120)

# ===== Memanggil Fungsi =====

# Persegi Panjang
persegi_panjang(150, 80)

t.penup()
t.goto(-200, 0)
t.pendown()

 # Segitiga
segitiga(100)

t.penup()
t.goto(0, -150)
t.pendown()

# Trapesium
trapesium(100, 150, 80)

t.penup()
t.goto(200, 0)
t.pendown()

# Jajar Genjang
jajar_genjang(120, 80)

t.penup()
t.goto(-200, -200)
t.pendown()

#Belah Ketupat
belah_ketupat(100)

turtle.done()