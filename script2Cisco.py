#import library telnetlib
import paramiko

import time 
#jika menggunakan waktu sleep cocok digunakan pada cisco

#buat variable untuk mendefinisikan IP, username dan password untuk SSH pada router
ip_add = '192.168.137.181' #ip address router, bisa diganti sesuai dengan yang ada di router
username = 'cisco' #username router, bisa diganti sesuai dengan yang ada di router
password = 'cisco' #password router, bisa diganti sesuai dengan yang ada di router

#buat variable untuk objek SSH server serta memanggil fungsi connect
ssh_tujuan = paramiko.SSHClient()
ssh_tujuan.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_tujuan.connect(ip_add, username=username, password=password)

#tampilkan pesan berhasil koneksi
print("Sukses Masuk Ke {}".format(ip_add))

conn = ssh_tujuan.invoke_shell() #memanggil fungsi invoke_shell untuk menjalankan perintah pada router


#fungsi untuk menjalankan perintah pada router
#bisa ditambahkan parameter untuk menjalankan perintah lainnya, ini hanya contoh
conn.send("conf t\n")
conn.send("int lo0\n")
conn.send("ip add 10.1.1.1 255.255.255.255\n")
time.sleep(1) #waktu ekseskusi perintah yang ditulis di router (1 detik) agar diberikan waktu untuk perintah tersebut saat dijalankan
#jika menggunakan paramiko wajib mensetting time sleep agar tidak terjadi error
#sehingga command cisco bisa terkirim dengan benar

output = conn.recv(65535) #mengambil output dari perintah yang ditulis di router
print(output.decode()) #menampilkan output dari perintah yang ditulis di router

#tutup program agar berhenti tereksekusi
ssh_tujuan.close()