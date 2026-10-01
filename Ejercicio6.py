from datetime import date
class ProductoKwike:
    def __eq__(self, other):
        if isinstance(other, ProductoKwike):
            return self.id_producto == other.id_producto and self.descripcion == other.descripcion
        return False
