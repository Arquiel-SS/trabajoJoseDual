from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Integrante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    genero = db.Column(db.String(80), nullable= False)
    fecha_formacion = db.Column(db.Date, nullable=False)
    integrante1 = db.Column(db.String(80), nullable = False )
    integrante2 = db.Column(db.String(80), nullable = False, default = None)
    integrante3 = db.Column(db.String(80), nullable = False, default = None)
    integrante4 = db.Column(db.String(80), nullable = False, default = None)
    integrante5 = db.Column(db.String(80), nullable = False, default = None)

    def get_integrante(self):
        return f"{self.integrante1}, {self.integrante2}, {self.integrante3}, {self.integrante4}, {self.integrante5}"
    def get_nombre(self):
        return self.nombre
    def get_genero(self):
        return self.genero
    def get_fecha(self):
        return self.fecha_formacion
    
    def set_integrantes(self, new):
        pass #se revisa
    


class Concierto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ubicacion = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.Date, nullable = False)
    grupo1 = db.Column(db.String(80), nullable = False)
    grupo2 = db.Column(db.String(80), nullable = False, default=None)
    grupo3 = db.Column(db.String(80), nullable = False, default=None)
    hora_inicio = db.Column(db.Time,nullable = False )
    hora_fin = db.Column(db.Time, nullable = False)
