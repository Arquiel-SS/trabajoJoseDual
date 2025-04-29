from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Integrante(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    apellidos=db.Column(db.String(80), nullable=False)
    edad=db.Column(db.Integer, nullable=False)
    nacionalidad=db.Column(db.String(80),nullable=False)
    fecha_nacimiento=db.Column(db.Date,nullable=False)
    rol=db.Column(db.String(80),nullable=False)

    def get_nombre(self):
        return self.nombre
    
    def get_apellidos(self):
        return self.apellidos
    
    def get_edad(self):
        return self.edad
    
    def get_nacionalidad(self):
        return self.nacionalidad
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def get_rol(self):
        return self.rol
    
    def set_nombre(self,new):
        self.nombre=new

    def set_apellidos(self,new):
        self.apellidos=new

    def set_edad(self,new):
        self.edad=new

    def set_nacionalidad(self,new):
        self.nacionalidad=new
    
    def set_fecha_nacimiento(self,new):
        self.fecha_nacimiento=new
    
    def set_rol(self,new):
        self.rol=new
   
class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Concierto(db.Model):
    id = db.Column(db.Integer, primary_key=True)