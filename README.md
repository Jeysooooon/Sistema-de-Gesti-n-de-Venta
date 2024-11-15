# Sistema de Gestión de Compras
Este proyecto es un sistema de gestión de compras que permite a los usuarios crear, leer, actualizar y eliminar (CRUD) usuarios, productos y compras. Está diseñado para facilitar la administración de un inventario de productos y las compras realizadas por los usuarios.

### Funcionalidades
- **Gestión de Usuarios**: Crear, leer, actualizar y eliminar usuarios.
- **Gestión de Productos**: Crear, leer, actualizar y eliminar productos.
- **Gestión de Compras**: Crear y leer compras, así como ver compras por usuario.

### Requisitos
- Python 3.x
- No se requieren bibliotecas externas para la funcionalidad básica.

### Directorio
   ```sh
   https://github.com/Jeysooooon/Sistema-de-Gesti-n-de-Venta/tree/Main2
  ```

## Gestión de Clientes
**Crear Cliente**:
  
  ```sh
Cliente.crear_cliente("nombre_cliente", "correo_cliente")
```
**Leer Cliente**:
  ```sh
clientes = Cliente.obtener_clientes(
```
**Actualizar Cliente**:
  ```sh
Cliente.actualizar_cliente(id_cliente, "nuevo_nombre", "nuevo_correo")
```
**Eliminar Cliente**:
  ```sh
Cliente.borrar_cliente(id_cliente)
```

## Gestión de Productos
**Crear Producto**:
  ```sh
Producto.crear_producto("nombre_producto", precio)
```
**Leer Producto**:
  ```sh
productos = Producto.obtener_productos()
```
**Actualizar Producto**:
  ```sh
Producto.actualizar_producto(id_producto, "nuevo_nombre", nuevo_precio)
```
**Eliminar Producto**:
  ```sh
Producto.borrar_producto(id_producto)
```

## Gestión de Ventas
**Crear Ventas**:
  ```sh
Venta.crear_venta(id_cliente, id_producto, cantidad)
```
**Leer Ventas**:
  ```sh
ventas = Venta.obtener_ventas()
```
**Leer Ventas por Cliente**:
  ```sh
ventas_cliente = Venta.obtener_ventas_por_cliente(id_cliente)  # Utiliza WHERE en la consulta SQL
```

## Consultas SQL
**Crear una Venta**:
  ```sh
INSERT INTO ventas (cliente_id, producto_id, cantidad, fecha) 
VALUES (123, 456, 2, '2024-11-15');  -- Reemplaza los valores según sea necesario
```
**Ver Todas las Ventas**:
  ```sh
SELECT * 
FROM ventas;
```
**Ver Ventas de un Cliente Específico**:
  ```sh
SELECT * 
FROM ventas 
WHERE cliente_id = 123;  -- Reemplaza 123 con el ID del cliente deseado
```
