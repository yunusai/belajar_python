from copy import deepcopy

info = {
    "nama": "Muhammad Yunus Saifullah",
    "universitas": "Universitas Dian Nuswantoro",
    "github": "github.com/yunusai",
    "jomblo": True,
    "hobi": ["menonton film dan anime", "main game", "menonton youtube", "membaca manga dan light novel"],
    "kulinerFavorit": {
        "makanan": "Nasi Goreng",
        "minuman": "Air Putih"
        }    
}

#pembuatan dictionary cara lain
warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")
print(warna_buah['apel'])

#output dictionary cara 1
print("\nOutput dictionary")
print("Nama: %s" % info["nama"])
print("Makanan Favorit: %s" % info["kulinerFavorit"]["makanan"])

#output dictionary cara 2
print("dapat dikontak melalui github di %s" % info.get("github"))
print("dan suka minum %s" % info["kulinerFavorit"].get("minuman"))

#loop
print("\nOutput dictionary menggunakan loop")
for i in info:
    print(info[i])

for i in info["kulinerFavorit"]:
    print("%s" % info["kulinerFavorit"][i])
    
#mengubah value dictionary
print("\nMengubah value dictionary")
info["jomblo"] = False
print("Apakah saya jomblo? %s"% info.get("jomblo"))

#Menghapus item dari dictionary
print("\nMenghapus item dari dictionary")
skill ={
    "utama" : "python",
    "lainnya": "php, dart, c++, html, css"
}
print(skill)

#menggunakan del
del skill["utama"]
print(skill)

#menggunakan pop
skill2 = {
    "utama" : "python",
    "lainnya" : "php, dart, c++, html, css"
}

print(skill2)
skill2.pop("utama")
print(skill2)

#menggunakan clear untuk menghapus dictionary secara keseluruhan
skill.clear()

#Menambah item ke dictionary
print("\nMenambahkan item di dictionary")
skill2.update({"utama" : "python"})
skill2.update({"lainnya": "php, dart, c++, html, css, java"})
print(skill2)

#mengcopy dictionary
#menggunakan copy(dictionary yang dicopy akan ikut terpengaruh)
print("\nMenggunakan copy(mempengaruhi dictionary asli)")
info2 = info.copy()
info2['nama'] = 'Yunus'
info2['hobi'].remove("membaca manga dan light novel")
print("\nData diri")
print(info)
print("\nData Diri 2")
print(info2)
#menggunakan deepcopy
print("\nMenggunakan deepcopy(tidak mempengaruhi dictionary asli)")
info3 = deepcopy(info)
info3['nama'] = 'Yunus Saifullah'
info3['hobi'].remove('menonton film dan anime')
print("\nData diri")
print(info)
print("\nData Diri 3")
print(info3)

#Mengetahui panjang dictionary
print("\nPanjang/Total data pada dictionary info: %d" % len(info))