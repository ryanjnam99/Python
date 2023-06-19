from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.persons import Person
from flask_app.models.recipes import Recipe
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/new/recipe')
def new_recipe():
    return render_template("add_recipe.html")

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    Recipe.save_recipe({**request.form, "person_id": session['id']})
    return redirect("/welcome")

