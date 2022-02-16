#import library telnetlib
import paramiko

#import time 
#jika menggunakan waktu sleep cocok digunakan pada cisco

#buat variable untuk mendefinisikan IP, username dan password untuk SSH pada router
ip_add = '192.168.137.144' #ip address router, bisa diganti sesuai dengan yang ada di router
username = 'admin' #username router, bisa diganti sesuai dengan yang ada di router``
password = '' #password router, bisa diganti sesuai dengan yang ada di router

#buat variable untuk objek SSH server serta memanggil fungsi connect
ssh_tujuan = paramiko.SSHClient()
ssh_tujuan.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_tujuan.connect(ip_add, username=username, password=password)

#tampilkan pesan berhasil koneksi
print("Sukses Masuk Ke {}".format(ip_add))

#fungsi untuk menjalankan perintah pada router
#bisa ditambahkan parameter untuk menjalankan perintah lainnya, ini hanya contoh
ssh_tujuan.exec_command("interface bridge add name loopback0\n")
ssh_tujuan.exec_command("ip address add address 10.2.2.1/32 interface=loopback0\n")

#tutup program agar berhenti tereksekusi
ssh_tujuan.close()