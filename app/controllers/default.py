from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from app import app, db, lm

from app.models.tables import User, Cliente
from app.models.forms import LoginForm, RegisterForm, PostForm, Registro


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login.")
    else:
        print(form.errors)
    return render_template('login.html', form = form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


@app.route('/register/', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            NewUserData = User(form.username.data,form.password.data,form.name.data,form.email.data)
            print(NewUserData)
            db.session.add(NewUserData)
            db.session.commit()
            return redirect(url_for("login"))
        except:
            return redirect(url_for("register"))
    else:
        print(form.errors)
    return render_template('register.html', form=form)


@app.route("/tables", methods=["GET","POST"])
def tables():
    client = Registro()
    if client.validate_on_submit():
        try:
            NewClient = Cliente(client.cpf.data,client.cliente.data,client.telefone.data,client.email_cli.data)
            print(NewClient)
            db.session.add(NewClient)
            db.session.commit()
            return redirect(url_for("tables"))
        except:
            return redirect(url_for("tables"))

#    if request.method == "POST":
        cpf = request.form.get("cpf")
        cliente = request.form.get("cliente")
        telefone = request.form.get("telefone")
        email_cli = request.form.get("email_cli")
#        if cpf and cliente and telefone and email_cli:
#            p = Cliente(cpf,cliente,telefone,email_cli)
#            db.session.add(p)
#            db.session.commit()

    else:
        print(client.errors)

    clientes = Cliente.query.all()

    return render_template('tables.html', client=client, clientes=clientes)
