hobi = []
stop = False
i = 0

while (not stop):
    hobi_baru = input("Masukkan hobi yang ke-{}:".format(i+1))
    hobi.append(hobi_baru)
    i+= 1
    tanya = input("Lanjut tambah hobi? (ya/tidak):")
    if(tanya == "tidak"):
        stop = True

print("="*20)
print("Kamu memiliki {} hobi".format(len(hobi)))
for i in hobi:
    print("- {}".format(i))
       
    