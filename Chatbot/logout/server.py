from flask import Flask,request

app = Flask(__name__)


@app.route('/log/',methods = ['POST'])
def login():
    data = request.get_json()
    
    try:
        ulasan = data.get('ulas')
        print(f"[INFO] =  Pesan Dari User: {ulasan}")
        return "Pesan Terkirim",200
    except Exception as e:
        print("Gagal",e)


if __name__ == "__main__":
    app.run(host= '192.168.0.101',debug=True)