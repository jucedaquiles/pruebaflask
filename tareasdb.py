from flask import Flask, render_template, request, redirect, url_for

import mysql.connector
import myDatabase


app = Flask(__name__)

@app.route("/")
def tareas():
    return render_template("lista.html", tareas=myDatabase.LeeDB(mydb))

@app.route("/add")
def add():
    tarea = request.args.get('tarea')
    myDatabase.EscribeDB(mydb, tarea)
    return redirect(url_for('tareas'))

@app.route("/delete/<int:tarea>")
def delete(tarea):
    myDatabase.BorraDB(mydb, tarea)
    return redirect(url_for('tareas'))

mydb = myDatabase.AbreDB()

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
