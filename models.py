from app import db

#create db model

class DataMhs(db.Model):
    NIM = db.Column(db.Integer, primary_key = True)
    Nama = db.Column(db.String(100), nullable = False)
    Jur = db.Column(db.String(150), nullable = False)

    #relationship to Nilai
    nilai = db.relationship('Nilai', backref = 'data_mhs', lazy = True)

    #buat function untuk mengakses class DataMhs
    def __repr__(self):
        return '<DataMhs {self.NIM}, {self.Nama}>'
    
class Matkul(db.Model):
    id_matkul = db.Column(db.Integer, primary_key = True)
    Nama_MK = db.Column(db.String(100), nullable = False)
    SKS = db.Column(db.Integer, nullable = False)

    #relationship to Nilai
    nilai = db.relationship('Nilai', backref = 'matkul', lazy = True)

    def __repr__(self):
        return '<Matkul {self.id_matkul}, {self.Matkul}>' 

class Nilai(db.Model):
    Nilai_id = db.Column(db.Integer, primary_key =  True)
    Nilai_NIM = db.Column(db.Integer, db.ForeignKey('data_mhs.NIM'), nullable = False)
    Nilai_id_matkul = db.Column(db.Integer, db.ForeignKey('matkul.id_matkul'), nullable = False)
    Nilai_Nilai = db.Column(db.Integer, nullable = True)
    Nilai_IPS = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'<Nilai {self.Nilai_NIM}, {self.Nilai_id_matkul}, {self.Nilai_Nilai}>'
    