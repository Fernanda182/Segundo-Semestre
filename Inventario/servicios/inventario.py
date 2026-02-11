# Importamos la clase Producto desde la carpeta modelos
from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar todos los productos.

    Se aplica el principio de responsabilidad única:
    - Producto representa la entidad.
    - Inventario gestiona las operaciones sobre los productos.
    """

    def __init__(self):
        """
        Constructor de la clase Inventario.

        Inicializa una lista vacía que almacenará objetos de tipo Producto.
        """
        self.productos = []  # Lista principal de almacenamiento

    # ------------------------------------------------
    # MÉTODO PARA AGREGAR PRODUCTO
    # ------------------------------------------------
    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Antes de añadirlo, se valida que no exista otro
        producto con el mismo ID.
        """

        # Recorremos la lista para verificar si el ID ya existe
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return False  # No se añade el producto

        # Si no existe, lo añadimos a la lista
        self.productos.append(producto)
        print("Producto añadido correctamente.")
        return True

    # ------------------------------------------------
    # MÉTODO PARA ELIMINAR PRODUCTO
    # ------------------------------------------------
    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario utilizando su ID.
        """

        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    # ------------------------------------------------
    # MÉTODO PARA ACTUALIZAR PRODUCTO
    # ------------------------------------------------
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Permite actualizar la cantidad y/o el precio de un producto.

        Parámetros opcionales:
        - nueva_cantidad: si no es None, se actualiza.
        - nuevo_precio: si no es None, se actualiza.
        """

        for p in self.productos:
            if p.get_id() == id_producto:

                # Solo actualiza si se proporciona valor
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("Producto actualizado correctamente.")
                return True

        print("Producto no encontrado.")
        return False

    # ------------------------------------------------
    # MÉTODO PARA BUSCAR PRODUCTOS
    # ------------------------------------------------
    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto indicado.
        La búsqueda no distingue entre mayúsculas y minúsculas.
        """

        resultados = []

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    # ------------------------------------------------
    # MÉTODO PARA MOSTRAR INVENTARIO COMPLETO
    # ------------------------------------------------
    def mostrar_inventario(self):
        """
        Muestra todos los productos almacenados.
        """

        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)