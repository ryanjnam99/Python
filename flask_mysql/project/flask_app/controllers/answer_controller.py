from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.users import User
from flask_app.models.answers import Answer
from flask import flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route("/start/craving")
def criteria_page():
    return render_template("answers.html")

@app.route("/save/answer")
def create_answer():
    data = {
        **request.form,
        "id": session['id']
    }
    Answer.save_answer(data)
    return redirect("/restaurants")