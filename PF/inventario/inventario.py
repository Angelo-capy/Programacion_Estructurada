from conexion_BD import Conectar_BD

def agregarinventario():
    conexion = Conectar_BD()
    if not conexion:
        return

    nombre = input("Nombre del producto: ").strip().upper()
    stock = int(input("Cantidad en stock: "))

    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO inventario (nombre_producto, unidades) VALUES (%s, %s)", (nombre, stock))
        conexion.commit()
        print("\n✅ Producto agregado al inventario.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conexion.close()

def consultarinventario():
    conexion = Conectar_BD()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario")
        productos = cursor.fetchall()

        print("\n📦 Inventario actual:")
        print(f"{'ID':<5}{'Producto':<20}{'Stock':<10}")
        for idp, nombre, unidades in productos:
            print(f"{idp:<5}{nombre:<20}{unidades:<10}")
    except Exception as e:
        print(f"❌ Error al consultar inventario: {e}")
    finally:
        conexion.close()
