# Importamos las clases necesarias
from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    """
    Muestra las opciones disponibles del sistema.
    """
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    """
    Función principal del programa.
    Aquí se ejecuta el menú interactivo.
    """

    # Creamos una instancia del inventario
    inventario = Inventario()

    # Bucle infinito hasta que el usuario decida salir
    while True:

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # ------------------------------------------------
        # OPCIÓN 1: AÑADIR PRODUCTO
        # ------------------------------------------------
        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                # Creamos el objeto Producto
                producto = Producto(id_producto, nombre, cantidad, precio)

                # Lo agregamos al inventario
                inventario.agregar_producto(producto)

            except ValueError:
                print("Error: Debe introducir valores numéricos válidos.")

        # ------------------------------------------------
        # OPCIÓN 2: ELIMINAR PRODUCTO
        # ------------------------------------------------
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # ------------------------------------------------
        # OPCIÓN 3: ACTUALIZAR PRODUCTO
        # ------------------------------------------------
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")

            try:
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                # Convertimos solo si el usuario introduce valor
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            except ValueError:
                print("Error en los valores introducidos.")

        # ------------------------------------------------
        # OPCIÓN 4: BUSCAR PRODUCTO
        # ------------------------------------------------
        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        # ------------------------------------------------
        # OPCIÓN 5: MOSTRAR INVENTARIO
        # ------------------------------------------------
        elif opcion == "5":
            inventario.mostrar_inventario()

        # ------------------------------------------------
        # OPCIÓN 6: SALIR
        # ------------------------------------------------
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()