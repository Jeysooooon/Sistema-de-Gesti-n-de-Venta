# Sistema de Gestion de Ventas
En este proyecto permite a los usuarios crear, leer, actualizar y eliminar (CRUD) usuarios, productos y compras. Está diseñado para facilitar la administración de un inventario de productos y las compras realizadas por los usuarios.

## Tabla de Contenidos
- [Introducción](#introducción)
- [Clases](#clases)
  - [Clase Usuario](#clase-usuario)
  - [Clase Producto](#clase-producto)
  - [Clase Compra](#clase-compra)
- [Métodos](#métodos)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción

Este proyecto es una aplicación para gestionar compras, usuarios y productos. Permite crear, leer y gestionar datos de manera eficiente.

## Clases

### Clase Usuario

La clase `Usuario` representa a un usuario en el sistema.

#### Atributos

- `id`: Identificador único del usuario.
- `nombre`: Nombre del usuario.
- `contraseña`: Contraseña del usuario.

#### Métodos

- `__init__(self, id, nombre, contraseña)`: Constructor de la clase.
- `crear_usuario(self)`: Crea un nuevo usuario en la base de datos.
- `obtener_usuarios()`: Devuelve una lista de todos los usuarios.

### Clase Producto

La clase `Producto` representa un producto en el sistema.

#### Atributos

- `id`: Identificador único del producto.
- `nombre`: Nombre del producto.
- `precio`: Precio del producto.

#### Métodos

- `__init__(self, id, nombre, precio)`: Constructor de la clase.
- `crear_producto(self)`: Crea un nuevo producto en la base de datos.
- `obtener_productos()`: Devuelve una lista de todos los productos.

### Clase Compra

La clase `Compra` representa una compra realizada por un usuario.

#### Atributos

- `id_usuario`: Identificador del usuario que realiza la compra.
- `id_producto`: Identificador del producto comprado.
- `cantidad`: Cantidad del producto comprado.

#### Métodos

- `__init__(self, id_usuario, id_producto, cantidad)`: Constructor de la clase.
- `crear_compra(self)`: Crea una nueva compra en la base de datos.
- `obtener_compras()`: Devuelve una lista de todas las compras.
- `obtener_compras_por_usuario(self, id_usuario)`: Devuelve las compras realizadas por un usuario específico.

## Métodos

- `menu()`: Muestra el menú principal de la aplicación.
- `menu_compras()`: Muestra el menú para gestionar compras.

## Repositorio

   ```sh  
   https://github.com/Jeysooooon/Sistema-de-Gesti-n-de-Venta
