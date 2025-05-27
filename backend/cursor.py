import sqlite3

conexion = sqlite3.connect('proyecto_grado/proyecto.db')
cursor = conexion.cursor()

cursor.execute("SELECT * FROM compra")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conexion.close()