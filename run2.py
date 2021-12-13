from flask import Flask
from flask import render_template
app = Flask(__name__)

posts = ['Joaquin', 'Paco']

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route("/carpeta/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=posts[int(slug)])

@app.route("/admin/post/")

@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)
    
    
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
        