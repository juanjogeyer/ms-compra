from app import db
from app.models import Compra

class CompraRepository:

    def add(self, compra: Compra) -> Compra:
        db.session.add(compra)
        db.session.commit()
        return compra

    def delete(self, id: int) -> Compra:
        compra = Compra.query.get(id)
        if compra:  # Verificamos si la compra existe
            db.session.delete(compra)  # Eliminar la compra
            db.session.commit()  # Confirmar los cambios en la base de datos
            return True  # Retornamos True si la eliminación fue exitosa
        return False  # Retornamos False si no se encontró la compra