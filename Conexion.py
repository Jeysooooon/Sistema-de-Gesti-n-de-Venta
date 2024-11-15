import mysql.connector

class ConexionBaseDatos:
    def __init__(self, host, usuario, contraseña, base_datos):
        self.conexion = mysql.connector.connect(
            host = host,
            user = usuario,
            password = contraseña,
            database = base_datos
        )
        self.cursor = self.conexion.cursor()
    
    def cerrar(self):
        self.cursor.close()
        self.conexion.close()
