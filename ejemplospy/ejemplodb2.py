import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="usuario",
  password="Audid4t%",
  database="pruebasflask"
)

mycursor = mydb.cursor()


#INSERTAR FILA
#sql = "INSERT INTO tareas (nombre_tarea, realizada) VALUES (%s, %s)"
sql = "INSERT INTO tareas (nombre_tarea, realizada) VALUES (%s, %s)"
Tarea=input("Nombre de la nueva tarea :")
val = (Tarea, False)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "Registro insertado.")


#MOSTRAR LAS FILAS
mycursor.execute("SELECT nombre_tarea FROM tareas ")
myresult = mycursor.fetchall()
print (type(myresult))
for x in myresult:
#  print (type(x))
  print(x[0])


#BORRAR UNA FILA
delTarea =  input ('Introduce el numero de tarea a borrar :')
sql = "DELETE FROM tareas WHERE nombre_tarea="+delTarea
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")