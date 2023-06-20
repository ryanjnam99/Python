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


@app.route('/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    data = {
        "id": recipe_id
    }
    certain_recipe = Recipe.get_recipe(data)
    return render_template("view_recipe.html", recipe=certain_recipe)

@app.route("/recipe/edit/<int:recipe_id>")
def edit_page(recipe_id):
    data = {
        "id": recipe_id
    }
    certain_recipe = Recipe.get_recipe(data)
    return render_template("edit_recipe.html", recipe=certain_recipe)

@app.route("/recipe/update/<int:recipe_id>", methods=['POST'])
def update(recipe_id):
    data = {
        **request.form,
        "id": recipe_id    
    }
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipe/edit/{recipe_id}")
    Recipe.edit_recipe(data)
    return redirect(f"/recipe/{recipe_id}")

@app.route("/recipe/delete/<int:recipe_id>")
def delete(recipe_id):
    data = {
        "id": recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect("/welcome")


