from app.repository import CompraRepository
from app.model import Compra
from typing import List

repository = CompraRepository()

class CompraService:

    def all(self) -> List[Compra]:
        return repository.all()

    def add(self, compra: Compra) -> Compra:
        return repository.add(compra)

    def delete(self, id: int) -> bool:
        compra = self.find(id)
        if compra:
            repository.delete(compra)
            return True
        else:
            return False

    def find(self, id: int) -> Compra:
        return repository.find(id)