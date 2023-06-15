from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo 

@app.route('/ninjas')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=all_dojos)
    return redirect('/ninja/create')

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')

    
# @app.route("/result")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("result.html")
#     # prints out the result within the form