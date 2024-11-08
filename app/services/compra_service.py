from app.compra_repository import CompraRepository
from app.models import Compra
from datetime import datetime

repository = CompraRepository()

class CompraService:

    def add(self, compra: Compra) -> Compra:
        compra.fecha_compra = datetime.now()
        result = repository.add(compra)
        return result

    def delete(self, id: int) -> Compra:
        result = repository.delete(id)
        return result