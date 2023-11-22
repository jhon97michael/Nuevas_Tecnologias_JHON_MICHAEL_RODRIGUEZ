import pymysql

class Usuario:
    def __init__(self, codigo, nombre, centrozonal, telefono, email):
        self._codigo = codigo
        self._nombre = nombre
        self._centrozonal = centrozonal
        self._telefono = telefono
        self._email = email

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def centrozonal(self):
        return self._centrozonal

    @property
    def telefono(self):
        return self._telefono

    @property
    def email(self):
        return self._email

class Defensora(Usuario):
    def __init__(self, codigo, nombre, centrozonal, telefono, email):
        super().__init__(codigo, nombre, centrozonal, telefono, email)

    # Puedes agregar más métodos específicos para las defensoras

class Profesional(Usuario):
    def __init__(self, codigo, nombre, apellido, profesion, telefono, email):
        super().__init__(codigo, nombre, None, telefono, email)  # No hay centrozonal para profesionales
        self._apellido = apellido
        self._profesion = profesion

    @property
    def apellido(self):
        return self._apellido

    @property
    def profesion(self):
        return self._profesion

class BaseDatos:
    def __init__(self, host, user, password, database):
        self._conexion = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self._conexion.cursor()

    def cerrar_conexion(self):
        self._cursor.close()
        self._conexion.close()

    def agregar_defensora(self, defensora):
        sql = "INSERT INTO defensoras (codigo_defensora, nombre_defensora, centrozonal_defensora, telefono_defensora, email_defensora) VALUES (%s, %s, %s, %s, %s)"
        values = (defensora.codigo, defensora.nombre, defensora.centrozonal, defensora.telefono, defensora.email)
        self._cursor.execute(sql, values)
        self._conexion.commit()
        pass

    def agregar_profesional(self, profesional):
        sql = "INSERT INTO profesional (ID_profesional, nombre_profesional, apellido_profesional, profesion_profesional, telefono_profesional, email_profesional) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (profesional.codigo, profesional.nombre, profesional.apellido, profesional.profesion, profesional.telefono, profesional.email)
        self._cursor.execute(sql, values)
        self._conexion.commit()
    pass

    def obtener_defensora_por_codigo(self, codigo_defensora):
        sql = "SELECT * FROM defensoras WHERE codigo_defensora = %s"
        self._cursor.execute(sql, (codigo_defensora,))
        result = self._cursor.fetchone()
        if result:
            return Defensora(
                result['codigo_defensora'],
                result['nombre_defensora'],
                result['centrozonal_defensora'],
                result['telefono_defensora'],
                result['email_defensora']
            )
        return None
    
    def obtener_profesional_por_codigo(self, codigo_profesional):
        sql = "SELECT * FROM profesional WHERE ID_profesional = %s"
        self._cursor.execute(sql, (codigo_profesional,))
        result = self._cursor.fetchone()
        if result:
            return Profesional(
                result['ID_profesional'],
                result['nombre_profesional'],
                result['apellido_profesional'],
                result['profesion_profesional'],
                result['telefono_profesional'],
                result['email_profesional']
            )


# Crear instancia de la base de datos
db = BaseDatos(host='localhost', user='root', password='', database='divina_providencia')

# Menú de inicio de sesión y creación de usuarios
while True:
    print("1. Iniciar sesión como defensora")
    print("2. Iniciar sesión como profesional")
    print("3. Crear cuenta de defensora")
    print("4. Crear cuenta de profesional")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == '1':
        # Iniciar sesión como defensora
        codigo_defensora = input("Ingrese su código de defensora: ")
        # Verificar credenciales y realizar acciones correspondientes

        defensora_encontrada =  db.obtener_defensora_por_codigo(codigo_defensora)
        if defensora_encontrada:
            print("Iniciaste sesión como defensora.")
            print("Datos de la defensora:")
            print(f"Código: {defensora_encontrada.codigo}")
            print(f"Nombre: {defensora_encontrada.nombre}")
            print(f"Centro Zonal: {defensora_encontrada.centrozonal}")
            print(f"Teléfono: {defensora_encontrada.telefono}")
            print(f"Email: {defensora_encontrada.email}")
        else:
            print("Código de defensora incorrecto.")
        
    elif opcion == '2':
        # Iniciar sesión como profesional
        codigo_profesional = input("Ingrese su código de profesional: ")
        
        profesional_encontrado = db.obtener_profesional_por_codigo(codigo_profesional)
        if profesional_encontrado:
            print("Iniciaste sesión como profesional.")
            print("Datos del profesional:")
            print(f"Código: {profesional_encontrado.codigo}")
            print(f"Nombre: {profesional_encontrado.nombre}")
            print(f"Apellido: {profesional_encontrado.apellido}")
            print(f"Profesión: {profesional_encontrado.profesion}")
            print(f"Teléfono: {profesional_encontrado.telefono}")
            print(f"Email: {profesional_encontrado.email}")
        else:
            print("Código de profesional incorrecto.")

    elif opcion == '3':
        # Crear cuenta de defensora
        codigo = input("Ingrese el código de la defensora: ")
        nombre = input("Ingrese el nombre de la defensora: ")
        centrozonal = input("Ingrese el centro zonal de la defensora: ")
        telefono = int(input("Ingrese el teléfono de la defensora: "))
        email = input("Ingrese el email de la defensora: ")

        nueva_defensora = Defensora(codigo, nombre, centrozonal, telefono, email)
        db.agregar_defensora(nueva_defensora)
        print("Cuenta de defensora creada exitosamente.")

    elif opcion == '4':
        # Crear cuenta de profesional
        codigo = input("Ingrese el código del profesional: ")
        nombre = input("Ingrese el nombre del profesional: ")
        apellido = input("Ingrese el apellido del profesional: ")
        profesion = input("Ingrese la profesión del profesional: ")
        telefono = int(input("Ingrese el teléfono del profesional: "))
        email = input("Ingrese el email del profesional: ")

        nuevo_profesional = Profesional(codigo, nombre, apellido, profesion, telefono, email)
        db.agregar_profesional(nuevo_profesional)
        print("Cuenta de profesional creada exitosamente.")

    elif opcion == '5':
        # Salir del programa
        db.cerrar_conexion()
        break

    else:
        print("Opción no válida. Intente nuevamente.")
