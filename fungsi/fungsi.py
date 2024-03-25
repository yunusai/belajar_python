#Membuat fungsi

#tanpa parameter
def aboutme():
    print("Dibuat oleh Muhammad Yunus Saifullah");
    print("https://github.com/yunusai");
    
aboutme();

#dengan parameter
def ucapan(input_nama):
    print("Halo, " + input_nama);
    print("Selamat datang di program ini");

ucapan("Yunus");

#dengan parameter tidak terbatas
def panggil(*nama):
    print("Daftar nama di kelas:");
    for panggilan in nama:
        print("-" + panggilan + "\n");
panggil("Yunus", "Ali", "Saiful", "Budi");

#dengan argumen default
def selamat(pesan, kata="Selamat anda beruntung"):
    print(kata, pesan);
selamat("Rita");
selamat("Anto", "Selamat anda berhasil");

#dengan perhitungan geometri
def luas_persegipanjang(panjang, lebar):
    return(panjang * lebar);
panjang = int(input("Masukkan panjang: "));
lebar = int(input("Masukkan lebar: "));
print("luas persegi panjang adalah: ", luas_persegipanjang(panjang, lebar));

#dengan if else
#tampilan menu
def show_menu():
    print("\n");
    print("Menu:");
    print("1. Show Data");
    print("2. Insert Data");
    print("3. Edit/Update Data");
    print("4. Delete Data");
    print("5. Exit");
    
    menu = int(input("Pilih menu: "));
    print("\n");
    
    if menu == 1:
        print("pilh submenu 1");
    elif menu == 2:
        print("pilih submenu 2");
    elif menu == 3:
        print("pilih submenu 3");
    elif menu == 4:
        print("pilih submenu 4");
    elif menu == 55:
        exit();
    else:
        print("Pilihan tidak tersedia");

show_menu();
    