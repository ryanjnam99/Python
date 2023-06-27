from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users import User
from flask_app.models.magazines import Magazine
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route("/add/magazine")
def new_magazine():
    return render_template("add_magazine.html")

@app.route("/create/magazine", methods=['POST'])
def create_magazine():
    if not Magazine.validate_magazine(request.form):
        return redirect("/add/magazine")
    Magazine.save_magazine({**request.form, "user_id":session['id']})
    return redirect("/welcome")

@app.route("/magazine/<int:magazine_id>")
def view_magazine(magazine_id):
    data = {
        "id": magazine_id
    }
    certain_magazine = Magazine.get_magazine(data)
    return render_template("view_magazine.html", magazine=certain_magazine)

@app.route("/magazine/delete/<int:magazine_id>")
def delete(magazine_id):
    data = {
        "id": magazine_id
    }
    Magazine.delete_magazine(data)
    return redirect("/welcome")



