import os
# fileobj = open('lokasi file','r+')

#buat file baru
f = open('file tes', 'w')
f.write('Baris pertama\n')
f.write('Baris kedua\n')
f.close()
print('File tersebut berada di', os.getcwd())

#membaca isi file
for i in range(2):
    print(str(i)+': '+f.readline())

a = ''
for char in f.read():
    a += char
print(a)

#mengganti nama file
os.rename('file tes','tes')

#Menghapus File
# os.remove('tes')

#Check ada tidaknya file
if os.path.isfile("tes")==True:
    print('File tes ada')
else:
    print('File tes tidak ada')