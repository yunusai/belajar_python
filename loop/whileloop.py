#bentuk umum
jawaban = "yes"
hitung = 0
while(jawaban == 'yes'):
    hitung +=1
    jawaban = input("Apakah anda ingin mengulang lagi? (yes/no) ")
    if jawaban == 'no':break
print("Total perulangan: ", hitung);