from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/kirim-ulasan',methods = ['POST'])

def terima_ulasan():
    try:
        data = request.get_json(force=True)
        print("Tipe Data:",type(data))
        print("Isi data",data)
        if not isinstance(data,dict):
            return jsonify({"message": "Format data tidak valid"}),400
        
        ulasan = data.get('ulasan','')
        print(f"Ulasan diterima: {ulasan}")
        

        
        with open("ulasan.txt","a") as f:
            f.write(ulasan + '\n\n\n')
            
        return jsonify({'message': 'ulasan berhasil di terima!'}),200
    except Exception as e:
        print("Error",e)
        return jsonify({"Message": f"Terjadi Kesalahan: {e}"}),400

@app.route('/file/tombol',methods = ['POST'])
def tombol():
    data = request.get_json()
    aktifitas = data.get('aktifitas')
    print(f"[INFO]: daftar Membaca:",aktifitas)
    return "Aktiftas diterima",200

@app.route('/file/log',methods = ['POST'])
def logout():
    data = request.get_json()
    aktifitas = data.get('keluar')
    print(f"[INFO] daftar user: ",aktifitas)
    return "User Keluar",200


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)


