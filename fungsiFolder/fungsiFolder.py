import os
#mengubah posisi folder aktif
os.mkdir("folder pythons")

#mengetahui nama folder aktif
print(os.getcwd())

#Menghapus Folder
os.rmdir("folder pythons")

#Check ada tidaknya folder
if os.path.isdir("/tmp")==True:
    print('Folder pythons ada')
else:
    print('Folder pythons tidak ada')