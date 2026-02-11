class Producto:
    """
    Clase que representa un producto dentro del sistema de inventario.

    Aplicamos encapsulamiento haciendo que los atributos sean privados
    (doble guion bajo __). De esta forma, solo se pueden modificar
    mediante métodos controlados (getters y setters).
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
        - id_producto: identificador único del producto.
        - nombre: nombre del producto.
        - cantidad: cantidad disponible en inventario.
        - precio: precio unitario del producto.
        """

        # Atributos privados
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ---------------------------
    # MÉTODOS GETTERS
    # ---------------------------

    def get_id(self):
        """Devuelve el ID del producto."""
        return self.__id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.__nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible."""
        return self.__cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.__precio

    # ---------------------------
    # MÉTODOS SETTERS
    # ---------------------------

    def set_nombre(self, nombre):
        """
        Modifica el nombre del producto.
        """
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Modifica la cantidad del producto.
        Se valida que la cantidad no sea negativa.
        """
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        """
        Modifica el precio del producto.
        Se valida que el precio no sea negativo.
        """
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    # ---------------------------
    # MÉTODO ESPECIAL
    # ---------------------------

    def __str__(self):
        """
        Método especial que define cómo se muestra el objeto
        cuando lo imprimimos con print().
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: {self.__precio:.2f}€"