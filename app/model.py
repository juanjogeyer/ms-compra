from app import db

class Compra(db.Model):
    __tablename__ = 'compras'

    id: int = db.Column(db.Integer, primary_key=True)
    producto_id: int = db.Column(db.Integer, nullable=False)
    fecha_compra = db.Column(db.DateTime, nullable=False)
    direccion_envio: str = db.Column(db.String(255), nullable=False)