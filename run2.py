from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#Para evitar ataques CSRF

posts = ['Joaquin', 'Paco']

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route("/lista")
def lista():
    return render_template("lista.html", lista=posts, nombre="Pepe")

@app.route("/carpeta/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=posts[int(slug)])

#@app.route("/admin/post/")
#@app.route("/admin/post/<int:post_id>/")

from forms import SignupForm, PostForm

@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)

        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=form)
    
from forms import SignupForm

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)
    
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
        