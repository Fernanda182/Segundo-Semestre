# Sistema de Gestión de Inventarios
## Autor: Fernanda Vaca

Este proyecto consiste en el desarrollo de un Sistema de Gestión de Inventarios en Python, diseñado para administrar los productos de una tienda mediante una aplicación de consola.

## El sistema permite:

- Añadir productos
- Eliminar productos
- Actualizar cantidad o precio
- Buscar productos por nombre
- Listar todos los productos del inventario

El desarrollo aplica los principios fundamentales de la Programación Orientada a Objetos (POO) y mantiene una arquitectura modular organizada por responsabilidades.

## Estructura del Proyecto
mi_inventario/
│
├── modelos/
│   └── producto.py
│
├── servicios/
│   └── inventario.py
│
└── main.py

## Diseño del Sistema
## Clase Producto

Representa la entidad principal del sistema.

## Atributos privados:
- ID (único)
- Nombre
- Cantidad
- Precio

## Métodos:
- Constructor
- Getters y setters
- Método __str__ para mostrar información formateada
- Se aplica encapsulamiento utilizando atributos privados.

## Clase Inventario

- Gestiona todos los productos.
- Estructura principal:
- Lista de objetos Producto

## Métodos implementados:

- agregar_producto()
- eliminar_producto()
- actualizar_producto()
- buscar_por_nombre()
- mostrar_inventario()

Se valida que no existan IDs duplicados antes de añadir un producto.

## Funcionamiento del Sistema

Al ejecutar el programa, se muestra el siguiente menú:

1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar inventario
6. Salir


