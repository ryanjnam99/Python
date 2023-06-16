from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.surveys import Survey


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("survey.html")

@app.route('/create/user', methods=['POST'])
def create_user():
    print("Got Post Info")
    if Survey.validate_survey(request.form):
        session['username'] = request.form['name']
        session['userplace'] = request.form['location']
        session['userlanguage'] = request.form['language']
        session['usercomment'] = request.form['comment']
        return redirect('/result')
    return redirect('/')


@app.route("/result")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")
    # prints out the result within the form
