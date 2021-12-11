#No funciona, no llega mi maquina al servidor Ubuntu pruebacookies que cree para las pruebas
#Dec  8 07:23:31 pruebascookies kernel: [33717.109150] [UFW BLOCK] IN=ens33 OUT= MAC=00:0c:29:24:94:ca:00:e1:8c:7c:68:75:08:00 SRC=192.168.0.10 DST=192.168.0.20 LEN=52 TOS=0x00 PREC=0x00 TTL=128 ID=41189 DF PROTO=TCP SPT=27013 DPT=5000 WINDOW=64240 RES=0x00 SYN URGP=0
#Permitir con ufw el acceso a la maquina 

#sudo ufw allow 5000
#Repetir la prueba y funciona


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
