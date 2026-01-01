from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

key = b"admin123"
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=key,iterations=100000,backend=default_backend())
key_a = base64.urlsafe_b64encode(kdf.derive(key))
cipher = Fernet(key_a)


class kode:
    def __init__(self,password):
        self.password = password
        self.fernet = cipher
        
    
    def halaman(self):
        user = input("apakah anda ingin membuka kode enkripsi?? [y/n]: ")
        enkripsi.tampilan(user)
    
    def tampilan(self,user):
        if "y" in user:
            encrp = self.fernet.encrypt(self.password)
            print(encrp)
        else:
            print("ya sudah")
            
    def page(self):
        tambah = input("Kode encryp: ")
        try:
            deskripsi_kode = self.fernet.decrypt(tambah)
            print(f"Hasil kode deks: {base64.urlsafe_b64decode(kdf.derive(deskripsi_kode))}")
        except Exception as e:
            print("gagal kode: ",e)

enkripsi = kode(key)
enkripsi.halaman()
enkripsi.page()

        