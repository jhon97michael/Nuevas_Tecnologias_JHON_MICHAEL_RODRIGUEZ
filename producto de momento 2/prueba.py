import mysql.connector

conexion = mysql.connector.connect(user='root', password='root',
                                    host='localhost',
                                    database='divina_providencia',
                                    port='3306')
print(conexion)
