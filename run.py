from flask import Flask
app = Flask(__name__)

#probando las listas

class rLista():
    Task=''
    End=True

_Lista=rLista()
_Lista.Task='Aprender python'
_Lista.End=False    

Filas=[_Lista]

_Lista.Task='Aprender FLASK'
_Lista.End=False    

Filas = Filas + [_Lista]

print(len(Filas))
print(Filas[0].Task)
print(Filas[1].Task)

@app.route("/")
def index():
    return "{} Filas".format(len(Filas))

#@app.route("/p/<string:slug>/")
#def show_post(slug):
#    return "Mostrando la Fila {}".format(slug)

@app.route("/carpeta/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=Filas[int(slug)].Task)    
    
# aqui estoy intentando entrar para ver como me contruye las url, usando el print, pero no se como entrar en el python
# con la aplicacion que esta corriendo para ir probando.

#print(url_for("index"))
#print(url_for("show_post", slug="leccion-1", preview=True))

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
        