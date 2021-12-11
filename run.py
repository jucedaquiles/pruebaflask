from flask import Flask
app = Flask(__name__)

#probando las listas

posts = ['Joaquin', 'Paco']

@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)
    
    
# aqui estoy intentando entrar para ver como me contruye las url, usando el print, pero no se como entrar en el python
# con la aplicacion que esta corriendo para ir probando.

#print(url_for("index"))
#print(url_for("show_post", slug="leccion-1", preview=True))

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
        