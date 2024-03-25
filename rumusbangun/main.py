import math
def persegipanjang():
    print("Kalkulator luas Persegi Panjang")
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    print("Luas persegi panjang adalah: ", p * l)
    print("Keliling persegi panjang adalah: ", 2 * (p + l))

def persegi():
    print("Kalkulator luas Persegi")
    s = int(input("Masukkan sisi: "))
    print("Luas persegi adalah: ", s * s)
    print("Keliling persegi adalah: ", 4 * s)

def segitiga():
    print("Kalkulator luas Segitiga")
    a = int(input("Masukkan alas: "))
    t = int(input("Masukkan tinggi: "))
    print("Luas segitiga adalah: ", 0.5 * a * t)
    print("Keliling segitiga adalah: ", 3 * a)
    
def layang():
    print("Kalkulator luas Layang-layang")
    d1 = int(input("Masukkan diagonal 1: "))
    d2 = int(input("Masukkan diagonal 2: "))
    print("Luas layang-layang adalah: ", 0.5 * d1 * d2)
    print("Keliling layang-layang adalah: ", 2 * (d1 + d2))

def trapesium():
    print("Kalkulator luas Trapesium")
    s1 = int(input("Masukkan sisi 1: "))
    s2 = int(input("Masukkan sisi 2: "))
    t = int(input("Masukkan tinggi: "))
    print("Luas trapesium adalah: ", 0.5 * (s1 + s2) * t)
    print("Keliling trapesium adalah: ", s1 + s2 + 2 * t)

def lingkaran():
    print("Kalkulator luas Lingkaran")
    r = int(input("Masukkan jari-jari: "))
    print("Luas lingkaran adalah: ", math.pi * r * r)
    print("Keliling lingkaran adalah: ", 2 * math.pi * r)

def bola():
    print("Kalkulator volume Bola")
    r = int(input("Masukkan jari-jari: "))
    print("Volume bola adalah: ", 4/3 * math.pi * r * r * r)
    print("Luas permukaan bola adalah: ", 4 * math.pi * r * r)
    
def balok():
    print("Kalkulator volume Balok")
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    t = int(input("Masukkan tinggi: "))
    print("Volume balok adalah: ", p * l * t)
    print("Luas permukaan balok adalah: ", 2 * (p * l + p * t + l * t))
    
def tabung():
    print("Kalkulator volume Tabung")
    r = int(input("Masukkan jari-jari: "))
    t = int(input("Masukkan tinggi: "))
    print("Volume tabung adalah: ", math.pi * r * r * t)
    print("Luas permukaan tabung adalah: ",2 * math.pi * r * (r + t))

def prisma():
    print("Kalkulator volume Prisma")
    a = int(input("Masukkan alas: "))
    t = int(input("Masukkan tinggi: "))
    print("Volume prisma adalah: ", 0.5 * a * t)
    print("Luas permukaan prisma adalah: ", 2 * a + 3 * t)
    
def limas():
    print("Kalkulator volume Limas")
    a = int(input("Masukkan alas: "))
    t = int(input("Masukkan tinggi: "))
    print("Volume limas adalah: ", 0.5 * a * t)
    print("Luas permukaan limas adalah: ", 2 * a + 3 * t)

def kerucut():
    print("Kalkulator volume Kerucut")
    r = int(input("Masukkan jari-jari: "))
    t = int(input("Masukkan tinggi: "))
    print("Volume kerucut adalah: ", 1/3 * math.pi * r * r * t)
    print("Luas permukaan kerucut adalah: ", math.pi * r * (r + math.sqrt(r * r + t * t)))
    
def kubus():
    print("Kalkulator volume Kubus")
    s = int(input("Masukkan sisi: "))
    print("Volume kubus adalah: ", s * s * s)
    print("Luas permukaan kubus adalah: ", 6 * s * s)

def show_menu():
    print("Menu:")
    print("1. Persegi Panjang")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Layang-layang")
    print("5. Trapesium")
    print("6. Lingkaran")
    print("7. Bola")
    print("8. Balok")
    print("9. Tabung")
    print("10. Prisma")
    print("11. Limas")
    print("12. Kerucut")
    print("13. Kubus")
    print("14. Exit")
    
    menu = int(input("Pilih menu: "))
    print("\n")
    
    if menu == 1:
        persegipanjang()
    elif menu == 2:
        persegi()
    elif menu == 3:
        segitiga()
    elif menu == 4:
        layang()
    elif menu == 5:
        trapesium()
    elif menu == 6:
        lingkaran()
    elif menu == 7:
        bola()
    elif menu == 8:
        balok()
    elif menu == 9:
        tabung()
    elif menu == 10:
        prisma()
    elif menu == 11:
        limas()
    elif menu == 12:
        kerucut()
    elif menu == 13:
        kubus()
    elif menu == 14:
        exit()
    else:
        print("Pilihan tidak tersedia")
        
print("Kalkulator Rumus Bangun Geometri")
jawab = "Yes"
while (jawab == "Yes"):
    show_menu()
    jawab = input("Kembali ke menu? (Yes/No) ")
    if jawab == "No":
        print("Terima kasih telah menggunakan kalkulator Rumus Bangun Geometri")
        break
    
