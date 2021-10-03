from flsite import Flask, render_template, request, flash, url_for, session, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdghsdkfjsdjkf12rkefh12r912hfasj9q219fhjso83611"


menu = [{'name': 'Установка', 'url': 'install-flash'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'Обратная связь', 'url': 'contact'}]

@app.route("/")
def index():
    return render_template("index.html", title = "Главная страница", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session["userLogged"] != username:
        abort(401)
    return f"Профиль пользователя {username}"

@app.route("/about")
def about():
    return render_template("about.html", title = "О нас")

@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Сообщение не отправлено", category="error")
        print(request.form)

    return render_template("contact.html", title = "Обратная связь", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

@app.route("/login", methods=["POST","GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for("profile", username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "admin" and request.form['psw'] == "123":
        session['userLogged'] = request.form["username"]
        return redirect(url_for("profile", username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)


