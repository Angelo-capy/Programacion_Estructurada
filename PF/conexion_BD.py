import mysql.connector
from mysql.connector import Error

def Conectar_BD():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            database='db_papeleria',
            user='root',
            password=''
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
