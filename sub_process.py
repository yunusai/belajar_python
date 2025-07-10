import subprocess
# berguna untuk memanggil program lain termasuk program jaringan.

# subprocess untuk memanggil ping
for ping in range(1, 10):
    alamat = "127.0.0." + str(ping)
    res = subprocess.call(['ping', alamat])
    if res == 0:
        print("ping ke", alamat, "berhasil")
    elif res == 2:
        print("tidak ada respon dari", alamat)
    else:
        print("ping ke", alamat, "gagal")