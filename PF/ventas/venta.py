from conexion_BD import Conectar_BD

def registrar_movimiento(id_usuario, id_producto, cantidad, tipo='salida'):
    conexion = Conectar_BD()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """INSERT INTO movimientos (id_usuario, id_producto, cantidad, tipo_movimiento)
                          VALUES (%s, %s, %s, %s)"""
            cursor.execute(consulta, (id_usuario, id_producto, cantidad, tipo))
            conexion.commit()
            print("\n🧾 Movimiento registrado correctamente.")
        except Exception as e:
            print(f"❌ Error al registrar movimiento: {e}")
        finally:
            conexion.close()

def hacer_venta(id_usuario):
    conexion = Conectar_BD()
    if not conexion:
        return

    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM inventario")
        productos = cursor.fetchall()
        if not productos:
            print("No hay productos disponibles.")
            return

        print("\n🛒 PRODUCTOS DISPONIBLES:")
        print(f"{'ID':<5}{'Producto':<20}{'Stock':<10}")
        for prod in productos:
            print(f"{prod['id_producto']:<5}{prod['nombre_producto']:<20}{prod['unidades']:<10}")

        id_producto = int(input("ID del producto a comprar: "))
        cantidad = int(input("Cantidad: "))

        cursor.execute("SELECT * FROM inventario WHERE id_producto = %s", (id_producto,))
        producto = cursor.fetchone()
        if not producto:
            print("Producto no encontrado.")
            return
        if cantidad > producto['unidades']:
            print("Stock insuficiente.")
            return

        registrar_movimiento(id_usuario, id_producto, cantidad)
        cursor.execute("UPDATE inventario SET unidades = unidades - %s WHERE id_producto = %s", (cantidad, id_producto))
        conexion.commit()
        print("\n✅ Venta realizada correctamente.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conexion.close()

def historial_movimientos():
    conexion = Conectar_BD()
    if not conexion:
        return
    try:
        cursor = conexion.cursor(dictionary=True)
        consulta = """
            SELECT m.id_movimiento, u.nombre AS usuario, i.nombre_producto AS producto,
                   m.cantidad, m.tipo_movimiento, m.fecha
            FROM movimientos m
            JOIN usuarios u ON m.id_usuario = u.id_usuario
            JOIN inventario i ON m.id_producto = i.id_producto
            ORDER BY m.fecha DESC
            LIMIT 10;
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print("\n🕘 Últimos movimientos:")
        print(f"{'ID':<4}{'Usuario':<15}{'Producto':<20}{'Cantidad':<10}{'Tipo':<10}{'Fecha'}")
        print("-"*70)
        for row in resultados:
            print(f"{row['id_movimiento']:<4}{row['usuario']:<15}{row['producto']:<20}{row['cantidad']:<10}{row['tipo_movimiento']:<10}{row['fecha']}")
    except Exception as e:
        print(f"❌ Error al consultar historial: {e}")
    finally:
        conexion.close()
