# Persegi
s = float(input("Masukkan sisi persegi: "))
print("Keliling persegi =", 4*s)
print("Luas persegi =", s*s)

# Persegi Panjang
p = float(input("\nMasukkan panjang: "))
l = float(input("Masukkan lebar: "))
print("Keliling persegi panjang=", 2*(p+l))
print("Luas persegi panjang =", p*l)

# Trapesium
a = float(input("\nMasukkan sisi atas: "))
b = float(input("Masukkan sisi bawah: "))
c = float(input("Masukkan sisi miring kiri:"))
d = float(input("Masukkan sisi miring kanan: "))
t = float(input("Masukkan tinggi: "))
print("Keliling trapesium =", a+b+c+d)
print("Luas trapesium =", (a+b)/2*t)