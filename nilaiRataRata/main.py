jumlah_elemen = 5
angka = []
sum = 0
for i in range(jumlah_elemen):
    value = eval(input("Masukkan angka: "))
    angka.append(value)
    sum += value
rata_rata = sum / jumlah_elemen
hitung = 0
for i in range(jumlah_elemen):
    if angka[i] > rata_rata:
        hitung += 1
print("Rata-ratanya adalah: ", rata_rata)
print("Banyak angka di atas rata-rata: ", hitung) 