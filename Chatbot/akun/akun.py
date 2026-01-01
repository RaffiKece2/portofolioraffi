from flask import Flask , jsonify, request
import sqlite3
import json
import os

app = Flask(__name__)

def ini_db():
    conn = sqlite3.connect("user.db")
    conn.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.commit()
    conn.close()



def login(username,password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user WHERE username= ? AND password = ? ',(username,password))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/file/akun',methods = ['POST'])
def akun():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'username dan password wajib diisi'})
    
    user = login(username,password)
    
    if user:
        print(f"[INFO] user {username} Loginnn")
        return jsonify({'message': f'Login berhasil ,halo {username}'}),200
    else:
        return jsonify({'message': 'login gagal, username dan password salah '}),401



@app.route('/file/register',methods = ['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": 'Username dan password wajib diisi'})
    
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    
    
    cursor.execute("SELECT * FROM user WHERE username = ?",(username,))
    if cursor.fetchone():
        return jsonify({"message": "Username sudah terdaftar"}),400
    
    cursor.execute("INSERT INTO user (username,password) VALUES (?,?)",(username,password))
    conn.commit()
    conn.close()
    
    return jsonify({"message": f"akun {username} berhasil register"}),201


FAVORIT_PATH = "favorit.json"

@app.route("/tambah_favorit", methods=["POST"])
def tambah_favorit():
    data = request.get_json()
    judul = data.get("judul")

    if not judul:
        return jsonify({"status": "error", "message": "Judul kosong"}), 400

    # Buat file jika belum ada
    if not os.path.exists(FAVORIT_PATH):
        with open(FAVORIT_PATH, "w") as f:
            json.dump([], f)

    # Tambahkan judul jika belum ada
    with open(FAVORIT_PATH, "r") as f:
        favorit = json.load(f)

    if judul not in favorit:
        favorit.append(judul)
        with open(FAVORIT_PATH, "w") as f:
            json.dump(favorit, f)

    return jsonify({"status": "success", "message": f"'{judul}' ditambahkan ke favorit."})

@app.route("/daftar_favorit", methods=["GET"])
def daftar_favorit():
    if not os.path.exists(FAVORIT_PATH):
        return jsonify([])

    with open(FAVORIT_PATH, "r") as f:
        favorit = json.load(f)
        print("[INFO] Daftar favorite = ", favorit)
    return jsonify(favorit)

if __name__ == "__main__":
    ini_db()
    app.run(host='0.0.0.0',port=5000,debug=True)
    