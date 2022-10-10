from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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