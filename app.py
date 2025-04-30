from flask import Flask, request, jsonify, render_template, redirect, url_for
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
        self.integrante1=new[0]

        if new[1] is not None:
            self.integrante2=new[1]
        
        if new[2] is not None:
            self.integrante3=new[2]

        if new[3] is not None:
            self.integrante4=new[3]

        if new[4] is not None:
            self.integrante5=new[4]

    def set_nombre(self,new):
        self.nombre=new

    def set_genero(self,new):
        self.genero=new

    def set_fecha(self,new):
        self.fecha_formacion=new
    


class Concierto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ubicacion = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.Date, nullable = False)
    grupo1 = db.Column(db.String(80), nullable = False)
    grupo2 = db.Column(db.String(80), nullable = False, default=None)
    grupo3 = db.Column(db.String(80), nullable = False, default=None)
    hora_inicio = db.Column(db.Time,nullable = False )
    hora_fin = db.Column(db.Time, nullable = False)

    def get_ubicacion(self):
        return self.ubicacion
    
    def get_fecha(self):
        return self.fecha
    
    def get_grupos(self):
        return f"{self.grupo1}, {self.grupo2}, {self.grupo3}"
    
    def get_horario(self):
        return f"{self.hora_inicio}, {self.hora_fin}"
    
    def set_ubicacion(self, new):
        self.ubicacion=new

    def set_fecha(self, new):
        self.fecha=new

    def set_grupos(self, new):
        self.grupo1=new[0]
        
        if new[1] is not None:
            self.grupo2=new[1]
        
        if new[2] is not None:
            self.grupo3=new[2]

    def set_horario(self, new):
        self.hora_inicio=new[0]
        self.hora_fin=new[1]


@app.route('/')
def mostrar_opciones_index():
    return render_template('index.html')

@app.route('/add_integrante', methods=["GET", "POST"])
def agregar_user():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        nacionalidad = request.form['nacionalidad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        rol = request.form['rol']

        return f"Gracias por añadir un integrante!"
    
    new_integrante = Integrante(nombre, apellidos, edad, nacionalidad, fecha_nacimiento, rol)
    db.session.add(new_integrante)
    db.session.commit()
    
    return render_template('integrantes.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)