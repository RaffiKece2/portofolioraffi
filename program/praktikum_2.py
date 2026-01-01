
# definisikan umur , tinggi dan siswa aktif dikonversi
def conversi(umur,tinggi_badan,siwa_aktif):
    # menumpulkan data kunci dan nilai
    seluru = {

        "umur: ": str(umur),
        "tinggi_badan: ": int(tinggi_badan),
        "siswa aktif: ": int(siwa_aktif)
    }

    # menulis kunci dan nilai dari data
    for key,value in seluru.items():
        print(key,value,"\n",type(key),type(value),"\n")

    # mengembalikan nilai
    return seluru
#menampilkan data
print(conversi(16,160.5,True))
