from flask import Flask, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy

from util import create_app, db
from models import cliente

app = create_app()

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
    return redirect("/clientes/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = cliente.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect("/clientes/")

@app.route("/actualizar/<int:id>/<nombre>/<apellido>/<direccion>/<telefono>")
def actualizar(id, nombre, apellido, direccion, telefono):
    p = cliente.query.filter_by(id=id).first()
    p.cliente_nombre = nombre
    p.cliente_apellido = apellido
    p.cliente_telefono = telefono
    db.session.commit()
    return redirect("/clientes/")

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
    app.run(debug=True, host='0.0.0.0')

