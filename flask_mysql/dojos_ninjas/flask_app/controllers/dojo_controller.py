from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojos import Dojo 
from flask_app.models.ninjas import Ninja



@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def everyone():
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.save(request.form)
    return redirect ("/dojos")

@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    data = {
        "id": dojo_id
    }
    certain_dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_ninjas.html", dojo=certain_dojo)


