x = 15
y = 4


seluru = {
    "tambah: ": x + y,
    "kurang: ": x - y,
    "kali: ": x * y,
    "pembagian: ": x / y,
    "Modul: ": x % y,
    "pangkat: ": x ** y,
    "Floor Division: ": x // y,
}

for key,value in seluru.items():
    print(key,value,"\n")
    