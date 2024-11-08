from marshmallow import Schema, fields, post_load
from app.models.compra import Compra

class CompraSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.Integer(required=True)
    fecha_compra = fields.DateTime(required=False)
    direccion_envio = fields.String(required=True)

    @post_load
    def make_compra(self, data, **kwargs):
        return Compra(**data)