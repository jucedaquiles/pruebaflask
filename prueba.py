from flask import Flask 

app= Flask(__name__)

@app.route('/')
def HelloWorld():
    # print ('<H1> Hello </H1>')
    return ('<H1> Hola mundo </H1>')

@app.route('/lista_de_tareas/')
def ListaDeTareas():
    return ('<H1> Aqui nos saldra el listado de la lista de tareas </H1>')

@app.route('/Esto_es_un_archivo')
def Daigual():
    return ('<H1> Al no terminar en / se descarga pero no es un archiv </H1>')
    
@app.route('/parametro/<Variable>')
def Parametros(Variable):
    return ('<H1> Aqui se muestran los parametros con Variable:{} </H1>'.format(Variable))
    
@app.errorhandler(404)
def Pagina_no_encontrada(Error):
    return ('<H1> Pagina no encontrada </H1>',404)
    
    


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
