from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.persons import Person
from flask_app.models.recipes import Recipe
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("person.html")

@app.route('/create/user', methods=['POST'])
def register():
    if not Person.validate_user(request.form):
        return redirect('/')
    if not Person.validate_email(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    data = {
        **request.form, 
        "password": pw_hash
    }
    user_id = Person.save(data)
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
    user_in_db = Person.get_by_email(data)
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
    one_user = Person.get_person(data)
    all_recipes = Recipe.get_all_recipes()
    return render_template("welcome.html",user=one_user, recipes=all_recipes)


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
    





