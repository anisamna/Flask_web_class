from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key_here'

#setting database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataAkademik.db'

#inisialisasi database
db = SQLAlchemy(app)

#import models setelah database
from models import DataMhs, Matkul, Nilai

#create all database tables
with app.app_context():
    db.create_all()

#default URL route saat flask run dieksekusi
@app.route('/')
def index():
    return render_template('index.html')

#alamat URL yang dituju saat menu "Home" diklik
@app.route('/index.html')
def index_html():
    return render_template('index.html')

#alamat URL yang dituju saat menu "SignUp" diklik
@app.route('/SignUp', methods = ['GET', 'POST'])
def SignUp(): 
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('pass')
        re_pass = request.form.get('re_pass')

        if password != re_pass:
            return "Password does not match, please try again !", 400
        
        print(f"Username: {username}, email: {email}, password: {password}")

        return redirect(url_for('index'))

    return render_template('SignUpUser.html')

#alamat URL saat menu "SignIn" di klik
@app.route('/SignIn', methods = ['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form.get('your_name')
        password = request.form.get('your_pass')

        """
        if username =="admin" and password == "admin123":
            return render_template('DataDiri.html', username="Admin")
        """
        if username and password:
            session['username'] = username
            return redirect(url_for('datadiri'))
        else:
            return render_template('SignInUser.html')
    return render_template('SignInUser.html')

"""
@app.route("/<page>")
def index_1(page="Grafik IPK"):
    # Pilih template berdasarkan halaman
    if page == "DataDiri":
        content_template = "Welcome.html"
    elif page == "KRS":
        content_template = "krs.html"
    elif page == "DaftarNilai":
        content_template = "daftar_nilai.html"
    elif page == "LaporanNilai":
        content_template = "laporan_nilai.html"
    elif page == "GrafikIPK":
        content_template = "grafik_ipk.html"
    else:
        content_template = "index.html"  # Default

    return render_template("index.html", page=page, content_template=content_template)
"""

@app.route('/DataDiri', methods = ['POST', 'GET'])
def datadiri():    
    if request.method == 'POST':
        #collect data dari tabel DataMhs, Matkul, Nilai
        NIM = request.form['NIM']
        Nama = request.form['Nama']
        Jur = request.form['Jur']
        ID_MK = int(request.form['id_matkul'])
        Nama_Matkul = request.form['Nama_MK']
        SKS = int(request.form['SKS'])
        Nil = int(request.form['Nilai_Nilai'])

        print(f'NIM: {NIM}, Nama: {Nama}, Jur: {Jur}, ID_MK: {ID_MK}, Nama_Matkul: {Nama_Matkul}, SKS: {SKS}, Nil: {Nil}')


        #create new record dari tabel DataMhs, Matkul, Nilai
        new_mhs = DataMhs(NIM=NIM, Nama=Nama, Jur=Jur)
        new_matkul = Matkul(Nama_MK=Nama_Matkul, SKS=SKS)

        #tambahkan record baru ke session dan lakukan commit database
        db.session.add(new_mhs)
        db.session.add(new_matkul)

        db.session.commit()

        #baru create record untuk table nilai setelah dapat PK dari table mhs dan matkul
        new_Nilai = Nilai(Nilai_NIM = NIM, Nilai_id_matkul = ID_MK, Nilai_Nilai = Nil)
        db.session.add(new_Nilai)

        db.session.commit()

        return redirect(url_for('datadiri'))
    
    mahasiswa = DataMhs.query.all()
    mataKuliah = Matkul.query.all()

    return render_template('DataDiri.html', mahasiswa = mahasiswa, mataKuliah = mataKuliah)
