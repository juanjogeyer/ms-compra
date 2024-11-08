from dataclasses import dataclass
import datetime
from app import db

class Compra(db.Model):
    __tablename__ = 'compras'

    id: int = db.Column(db.Integer, primary_key=True)
    producto: int = db.Column("producto_id", db.Integer, nullable=False)
    fecha_compra: datetime = db.Column(db.DateTime, nullable=False)
    direccion_envio: str = db.Column(db.String(120), nullable=False)