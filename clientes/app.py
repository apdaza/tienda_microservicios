from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SECRET_KEY'] = "123"

db = SQLAlchemy(app)

class cliente(db.Model):
    id  = db.Column("cliente_id", db.Integer, primary_key=True)
    cliente_nombre = db.Column(db.String(50))
    cliente_apellido = db.Column(db.String(50))
    cliente_direccion = db.Column(db.String(300))
    cliente_telefono = db.Column(db.String(20))

    def __init__(self, datos):
        self.cliente_nombre = datos['nombre']
        self.cliente_apellido = datos['apellido']
        self.cliente_direccion = datos['direccion']
        self.cliente_telefono = datos['telefono']

@app.route("/")
def principal():
    data = cliente.query.all()
    diccionario_clientes = {}
    for d in data:
        p = {"id": d.id,
             "nombre": d.cliente_nombre,
             "apellido": d.cliente_apellido,
             "direccion": d.cliente_direccion,
             "telefono": d.cliente_telefono
            }
        diccionario_clientes[d.id] = p
    return diccionario_clientes

@app.route("/agregar/<nombre>/<apellido>/<direccion>/<telefono>")
def agregar(nombre, apellido, direccion, telefono):
    datos = {"nombre": nombre,
             "apellido": apellido,
             "direccion": direccion,
             "telefono": telefono
            }
    p = cliente(datos)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = cliente.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/actualizar/<int:id>/<nombre>/<apellido>/<direccion>/<telefono>")
def actualizar(id, nombre, apellido, direccion, telefono):
    p = cliente.query.filter_by(id=id).first()
    p.cliente_nombre = nombre
    p.cliente_apellido = apellido
    p.cliente_telefono = telefono
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/buscar/<int:id>")
def buscar(id):
    d = cliente.query.filter_by(id=id).first()
    p = {"id": d.id,
         "nombre": d.cliente_nombre,
         "apellido": d.cliente_apellido,
         "direccion": d.cliente_direccion,
         "telefono": d.cliente_telefono
        }
    return p


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')

