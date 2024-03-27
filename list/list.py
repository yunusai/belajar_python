buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

print(buah[2])

my_friends = ["Yoga", "Septi", "Budi", "Diah", "Dika"]

print("isi my_friends index ke 3 adalah {}".format(my_friends[3]))

print("teman saya ada {} orang".format(len(my_friends)))
for friend in my_friends:
    print(friend)

#Mengubah item dalam list
print("\nMengubah item dalam list")
buah[2] = "Kelapa"
for namabuah in buah:
    print(namabuah)

#Menambah item dalam list
#Append(ditambah di akhir)
print("\nMenambah item dalam list metode append")
buah.append("Salak")
for namabuah in buah:
    print(namabuah)

#insert (menambah data pada index tertentu)
print("\nMenambah item dalam list metode insert")
buah.insert(2, "Jeruk")

for namabuah in buah:
    print(namabuah)
    
#Hapus item menggunakan del
print("\nMenghapus item dalam list dengan del")
del buah[2]

for namabuah in buah:
    print(namabuah)
    
#Hapus item menggunakan remove
print("\nMenghapus item dalam list dengan remove")
buah.remove("Kelapa")

for namabuah in buah:
    print(namabuah)
    
#Menghapus menggunakan pop(hanya menghapus index terakhir)
print("\nMenghapus menggunakan pop(hanya menghapus index terakhir)")
buah.pop()

for namabuah in buah:
    print(namabuah)
    
#Reverse isi list
print("\nReverse isi list")
buah.reverse()

for namabuah in buah:
    print(namabuah)
    
#Mengurutkan nilai isi list
print("\nMengurutkan nilai isi list")
nilaix = [3, 4, 5, 1, 2, 2, 10, 23]
nilaiy = nilaix[:] #Mengkopi list x ke y
nilaiy.sort()
print(nilaix)
print(nilaiy)

#mengurutkan nilai isi list menggunakan sorted
print("\nMengurutkan nilai isi list menggunakan sorted")
nilaiy2 = sorted(nilaix)
print(nilaix)
print(nilaiy2)

#Memotong/Divide list
print("\nMemotong/Divide list(Mencetak isi list dengan rentang index yang diinginkan)")
print (nilaiy [3: 6]) #Mengambil nilai index 3 sampai 5


#Operasi pada list
#Penggabungan
list_lagu = [
    "Dear God",
    "Its My Life"
]

playlist_favorit = [
    "Fireflies",
    "Im Still Standing"
]

semua_lagu = list_lagu + playlist_favorit

print("\nOperasi Penggabungan")
print(semua_lagu)

#Perkalian
ulang = 5
now_playing = semua_lagu * ulang
print("\nOperasi Perkalian")
print(now_playing)

print(len(nilaix))
print(max(nilaix))
print(min(nilaix))
print(sum(nilaix))


