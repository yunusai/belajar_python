import os
# memanggil program konsul lain
# hasil dapat ditampilkan melalui perintah print

ip = input("Target IP: ")
results=os.popen("pathping " + str(ip))
for i in results:
    print(i.strip())