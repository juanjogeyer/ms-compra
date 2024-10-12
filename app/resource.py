from flask import Blueprint, request
from marshmallow import ValidationError
from .mapping import CompraSchema, ResponseSchema
from .services import CompraService, ResponseBuilder

compra = Blueprint('compra', __name__)

compra_service = CompraService()
compra_schema = CompraSchema()
response_schema = ResponseSchema()

@compra.route('/compras', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    compras = compra_service.all()
    data = compra_schema.dump(compras, many=True)
    response_builder.add_message("Compras encontradas").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@compra.route('/compras', methods=['POST']) 
def add():
    response_builder = ResponseBuilder()
    try:
        compra = compra_schema.load(request.json)
        data = compra_schema.dump(compra_service.add(compra))
        response_builder.add_message("Compra added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@compra.route('/compras/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = compra_service.delete(id)
    if data:
        response_builder.add_message("Compra deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Compra not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404