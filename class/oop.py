class orang:
    def __init__(self, nama):
        self.nama = nama
    
    def katakanHalo(self):
        print("Halo, nama saya %s" % self.nama)

org = orang("Yunus")
org.katakanHalo()

class Makanan:
    __about = "Created by Yunus"
    __menu = ""
    nama = ""
    def __init__(self,nama):
        self.nama = nama
    def get__about(self):
        print(self.__about)
        print("Yang dipesan: %s" % self.__menu)
    def set_food(self, isi):
        if(isi == "sate kambing"):
            print("Sate kambing enak dan tinggi kolestrol")
        elif(isi == "nasi goreng"):
            print("Favorit sejuta umat")
        elif(isi == "mi goreng"):
            print("Favorit 8 milyar umat")
        else:
            print("Anda niat makan gk?")
        self.__menu = isi
m = Makanan("Malam")
m.set_food("mi goreng")
m.get__about()