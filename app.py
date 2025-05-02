from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    integrantes=Integrante.query.all()
    grupos=Grupo.query.all()
    return render_template('index.html',integrantes=integrantes,grupos=grupos)

@app.route('/crear_integrante', methods=["GET", "POST"])
def crear_integrante():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        nacionalidad = request.form['nacionalidad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        rol = request.form['rol']
        new_integrante = Integrante(nombre, apellidos, edad, nacionalidad, fecha_nacimiento, rol)
        db.session.add(new_integrante)
        db.session.commit()

        return f"Gracias por añadir un integrante!"
    
    
    return render_template('integrantes.html')

@app.route('/crear_grupo', methods=["GET", "POST"])
def crear_grupo():
    integrantes = Integrante.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        
        fecha_formacion_str = request.form['fecha_formacion']
        fecha_formacion = datetime.strptime(fecha_formacion_str, '%Y-%m-%d').date()
        
        integrante1 = request.form['integrante1']
        integrante2 = request.form.get('integrante2', None)
        integrante3 = request.form.get('integrante3', None)
        integrante4 = request.form.get('integrante4', None)
        integrante5 = request.form.get('integrante5', None)

        nuevo_grupo = Grupo(
            nombre=nombre,
            genero=genero,
            fecha_formacion=fecha_formacion,
            integrante1=integrante1,
            integrante2=integrante2,
            integrante3=integrante3,
            integrante4=integrante4,
            integrante5=integrante5
        )
        db.session.add(nuevo_grupo)
        db.session.commit()

        return "Gracias por añadir un grupo!"

    return render_template('grupos.html', integrantes=integrantes)

@app.route('/crear_concierto', methods=["GET", "POST"])
def crear_concierto():
    grupos=Grupo.query.all()
    if request.method == "POST":
        ubicacion = request.form['ubicacion']
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        grupo1 = request.form['grupo1']
        grupo2 = request.form.get('grupo2', None)
        grupo3 = request.form.get('grupo3', None)
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']

        # Convierte las horas de formato HH:MM a objetos time
        hora_inicio_str = request.form['hora_inicio']
        hora_fin_str = request.form['hora_fin']
        
        # Usamos strptime para convertir la cadena en un objeto time
        hora_inicio = datetime.strptime(hora_inicio_str, '%H:%M').time()
        hora_fin = datetime.strptime(hora_fin_str, '%H:%M').time()
        
        new_concierto = Concierto(
            ubicacion=ubicacion, 
            fecha=fecha, 
            grupo1=grupo1, 
            grupo2=grupo2,
            grupo3=grupo3,
            hora_inicio=hora_inicio, 
            hora_fin=hora_fin
            )
        db.session.add(new_concierto)
        db.session.commit()

        return f"Gracias por añadir un integrante!"
    
    return render_template('conciertos.html',grupos=grupos)

@app.route('/integrantes/<id>')
def get_integrante_by_id(id):
    integrante=Integrante.query.get(id)
    grupos=Grupo.query.all()
    gruposWhereIntegranteIs=[]
    if not grupos:
        return "No hay grupos creados"
    elif integrante is not None:
        for grupo in grupos:
            match(integrante.nombre):
                case grupo.integrante1:
                    gruposWhereIntegranteIs.append(grupo.nombre)
                case grupo.integrante2:
                    gruposWhereIntegranteIs.append(grupo.nombre)
                case grupo.integrante3:
                    gruposWhereIntegranteIs.append(grupo.nombre)
                case grupo.integrante4:
                    gruposWhereIntegranteIs.append(grupo.nombre)
                case grupo.integrante5:
                    gruposWhereIntegranteIs.append(grupo.nombre)
                case _:
                    pass
        if len(gruposWhereIntegranteIs)==0:
            gruposWhereIntegranteIs.append("No esta en ningun grupo")
        return render_template('get_integrante.html',integrante=integrante,grupos=gruposWhereIntegranteIs)
    else:
        return f"No se ha encontrado el integrante con id {id}"
    

@app.route('/ver_informacion', methods=['GET', 'POST'])
def ver_informacion():
    integrantes = Integrante.query.all()
    grupos = Grupo.query.all()
    conciertos = Concierto.query.all()
    filtro_resultado = []
    filtro_tipo = None

    if request.method == 'POST':
        filtro_tipo = request.form['filtro_tipo']
        filtro_valor = request.form['filtro_valor']

        if filtro_tipo == 'grupo':
            grupo = Grupo.query.get(filtro_valor)
            if grupo:
                filtro_resultado = [c for c in conciertos if c.grupo1 == grupo.nombre or c.grupo2 == grupo.nombre or c.grupo3 == grupo.nombre]
            else:
                filtro_resultado = []

        elif filtro_tipo == 'integrante':
            integrante = Integrante.query.get(filtro_valor)
            gruposWhereIntegranteIs = []

            if integrante is not None and grupos:
                for grupo in grupos:
                    # Verificamos si el integrante está en algún grupo
                    if integrante.nombre in [grupo.integrante1, grupo.integrante2, grupo.integrante3, grupo.integrante4, grupo.integrante5]:
                        gruposWhereIntegranteIs.append(grupo)
                
                if len(gruposWhereIntegranteIs) == 0:
                    gruposWhereIntegranteIs.append(
                        Grupo(nombre="No está en ningún grupo", genero="N/A")
                    )
                filtro_resultado = gruposWhereIntegranteIs
            else:
                filtro_resultado = [Grupo(nombre=f"No se ha encontrado el integrante con id {filtro_valor}", genero="N/A")]

    return render_template('ver_informacion.html',
                           integrantes=integrantes,
                           grupos=grupos,
                           conciertos=conciertos,
                           filtro_resultado=filtro_resultado,
                           filtro_tipo=filtro_tipo)


@app.route('/grupos/<id>')
def get_grupo_by_id(id):
    grupo = Grupo.query.get(id)
    conciertos = Concierto.query.all()
    conciertos_del_grupo = []

    if grupo is None:
        return f"No se ha encontrado el grupo con id {id}"

    for concierto in conciertos:
        if grupo.nombre in [concierto.grupo1, concierto.grupo2, concierto.grupo3]:
            conciertos_del_grupo.append(f"{concierto.fecha} en {concierto.ubicacion} (de {concierto.hora_inicio} a {concierto.hora_fin})")

    if not conciertos_del_grupo:
        conciertos_del_grupo.append("Este grupo no tiene conciertos registrados.")

    return render_template('get_grupo.html', grupo=grupo, conciertos=conciertos_del_grupo)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)