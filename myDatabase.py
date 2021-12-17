#Modulo para la gestion de la BD. No implementada totalmente abstracta, aun me queda que investigar-

import mysql.connector

def AbreDB():
    return (mysql.connector.connect( host='localhost', user= 'usuario', passwd='Audid4t%', db='pruebasflask' ))

#Lee un cursor desde un comienzo 'ini' un numero de filas 'filas'
def LeeDB(db, ini=1, filas=10) :
    mycursor = db.cursor()
    mycursor.execute("SELECT id, nombre_tarea FROM tareas ")
    ListaTareas = mycursor.fetchall()
    mycursor.close()
    return ListaTareas

def EscribeDB(db, fila) :
    mycursor = db.cursor()
    sql = "INSERT INTO tareas (nombre_tarea, realizada) VALUES (%s, %s)"
    val = (fila, False)
    mycursor.execute(sql, val)
    db.commit()
    mycursor.close()

def BorraDB(db, fila) :
    mycursor = db.cursor()
    sql = "DELETE FROM tareas WHERE id = %s "
    mycursor.execute(sql, (fila,))
    db.commit()
    mycursor.close()
