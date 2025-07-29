from conexion_BD import Conectar_BD

def insertar_usuario(nombre, apellido, correo, contrasena, celular):
    conexion = Conectar_BD()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """INSERT INTO usuarios (nombre, apellido, correo_electronico, contrasena, celular)
                          VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(consulta, (nombre, apellido, correo, contrasena, celular))
            conexion.commit()
            print("\n✅ Usuario registrado correctamente.")
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
        finally:
            conexion.close()

def iniciar_sesion():
    conexion = Conectar_BD()
    if not conexion:
        return None

    cursor = conexion.cursor(dictionary=True)
    correo = input("📧 Correo electrónico: ").strip()
    contrasena = input("🔐 Contraseña: ").strip()

    try:
        cursor.execute("SELECT * FROM usuarios WHERE correo_electronico = %s AND contrasena = %s", (correo, contrasena))
        usuario = cursor.fetchone()
        if usuario:
            print(f"\n✅ ¡Bienvenido {usuario['nombre']}!")
            return usuario
        else:
            print("❌ Correo o contraseña incorrectos.")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    finally:
        conexion.close()
