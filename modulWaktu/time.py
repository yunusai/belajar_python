import datetime
import time

sekarang = datetime.datetime.now()

tanggal = sekarang.date()
waktu = sekarang.time()

print("Hari: ", tanggal.day)
print("Bulan: ", tanggal.month)
print("Tahun: ", tanggal.year)
print("Jam: ", waktu.hour)
print("Menit: ", waktu.minute)
print("Detik: ", waktu.second)

time.sleep(5)

sekarang2 = datetime.datetime.now()
selisih = sekarang2 - sekarang
print("Selisih detik: ", selisih.total_seconds())