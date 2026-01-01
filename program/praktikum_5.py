import  random

nama = "Raffi Putra"

angka_nilai = [90.0,87.5,75.5,60.0]

lulus = True

nilai = random.choices(angka_nilai)

if nilai[0] > 60.0:
    print("siswa mendapatkan nilai: ",nilai)
    print("lulus: ",lulus)
else:
    lulus = False
    print("lulus: ",lulus)



