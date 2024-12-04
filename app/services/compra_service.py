from app.compra_repository import CompraRepository
from app.models import Compra
from datetime import datetime
from app import cache

repository = CompraRepository()

class CompraService:

    def add(self, compra: Compra) -> Compra:
        compra.fecha_compra = datetime.now()
        result = repository.add(compra)
        cache.set(f"compra_{result.id}", result, timeout=60)
        return result

    def delete(self, id: int) -> Compra:
        cache.delete(f"compra_{id}")
        result = repository.delete(id)
        return result