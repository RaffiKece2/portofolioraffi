

nama = "Raffi Putra" #harus ada tanda kutip seperti ""
umur = 21 #umur harus integer bukan string
berat = 60.4  #ini juga harus float bukan string
tinggi = 170 #ini bisa langsung integer juga bisa float
bmi = int(berat) / ((tinggi / 100) ** 2) #ini sudah benar
status_siswa = True  #ini tidak memakai string karena tipe nya boolean bukan string


data = {
    "nama: ": nama,
    "umur: ": (int(umur) + 1 ,"tahun"),
    "berat: ": (berat,"kg"),
    "tinggi: ": tinggi,
    "BMI: ": round(bmi,2),
    "status_siswa: ": bool(status_siswa)
}

for kunci,nilai in data.items():
    print(kunci,nilai,"\n")