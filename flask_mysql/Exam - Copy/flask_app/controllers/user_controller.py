from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users import User
from flask_app.models.magazines import Magazine
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)


# our index route will handle rendering our form
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
    data = {
        'id': session['id']
    }
    one_user = User.get_user(data)
    all_magazines = Magazine.get_all_magazines()
    return render_template("welcome.html",user=one_user, magazines=all_magazines)

@app.route("/user/account/<int:user_id>")
def view_account(user_id):
    data = {
        **request.form,
        "id": user_id
    }
    one_user = User.get_user(data)
    one_author = User.get_user_with_magazines(data)
    one_magazine = Magazine.get_all_magazines()
    return render_template("view_account.html", user=one_user, author=one_author, magazine=one_magazine)

@app.route("/user/update/<int:user_id>", methods=['POST'])
def edit_account(user_id):
    data = {
        **request.form,
        "id": user_id
    }
    if not User.validate_update(request.form):
        return redirect(f"/user/account/{user_id}")
    User.edit_user(data)
    return redirect(f"/user/account/{user_id}")
    
    

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

    




