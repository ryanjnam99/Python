from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users import User
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template("registration.html")

@app.route('/create/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    if not User.validate_email(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    data = {
        **request.form, 
        "password": pw_hash
    }
    user_id = User.save(data)
    session['id'] = user_id
    return redirect("/welcome")

@app.route('/login/page')
def go_to_login():
    return render_template("login.html")



@app.route("/login/user", methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if len(request.form['password']) < 4:
        flash("Invalid Email/Password")
        return redirect("/login/page")
    pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login/page")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login/page')
    session['id'] = user_in_db.id
    return redirect("/welcome")

@app.route("/welcome")
def welcome():
    if 'id' not in session:
        return redirect ('/')
    data = {
        'id': session['id']
    }
    one_user = User.get_user(data)
    return render_template("welcome.html",user=one_user)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
    





