print ("Resultados de mysql.connector:")

import mysql.connector

miConexion = mysql.connector.connect( host='localhost', user= 'usuario', passwd='Audid4t%', db='pruebasflask' )

print (type(miConexion))

cur = miConexion.cursor()

cur.execute( "SELECT nombre_tarea, realizada FROM tareas" )

for nombre_tarea, realizada in cur.fetchall() :
    print (nombre_tarea, realizada)

cur.execute('INSERT INTO tareas (nombre_tarea, realizada) VALUES (%s, %s)', ('Hacer varias pruebas', True))

miConexion.commit()
    
for nombre_tarea, realizada in cur.fetchall() :
    print (nombre_tarea, realizada)
        
miConexion.close()
