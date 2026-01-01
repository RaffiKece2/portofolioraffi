import requests
from cryptography.fernet import Fernet

key = Fernet.generate_key()
chiper = Fernet(key)



class Kode:
    def halaman(self):
        data = input('Ketik: ')
        if data == "pesan":
            kode.pesan()
        elif data == "login":
            kode.login()
            
    def pesan(self):
            data = input("Ketik: ")
            try:
                pose = requests.post("http://192.168.0.105:5000/file/log",json={'ulas': data})
                if pose.status_code == 200:
                    print("Pesan Terkirim")
            except requests.exceptions.RequestException as e:
                print('Gagal', e)
    
    def login(self):
        while True:
            user = input("Username: ")
            password = input("Password: ").encode()
            pass_hash = chiper.encrypt(password)
            
            try:
                data = requests.post("http://192.168.0.105:5000/file/akun",json={'username': user,'pass_hash': pass_hash})
                if data.status_code == 200:
                    print("Akun Anda Masuk")
                else:
                    print("Gagal Menerima Akun")
            except Exception as e:
                print("Server Gagal",e)                    
kode = Kode()

kode.halaman()
        