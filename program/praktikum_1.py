
#mendefinisikan identitas yang isinya ada nama,usia,tinggi dan siswa aktif
def identitas(nama,usia,tinggi_badan,siwa_aktif):

    print("nama: ",nama, "Tipe: ",type(nama)) #string
    print("usia: ",usia, "Tipe: ",type(usia)) #integer
    print("Tinggi Badan: ",tinggi_badan, "Tipe: ",type(tinggi_badan)) #float
    print("siswa Aktif: ",siwa_aktif,type(siwa_aktif)) #boolean

    # mengembalikan nilai agar tidak None
    return nama,usia,tinggi_badan,siwa_aktif

#menampilkan output atau nilai
print(identitas("M.Raffi Putra Umaryono",16,160.5,True))

