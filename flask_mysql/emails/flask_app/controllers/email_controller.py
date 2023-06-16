from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.emails import Email


# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("email.html")

@app.route('/create/email', methods=['POST'])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect("/show/emails")

@app.route('/show/emails')
def everyone():
    all_emails = Email.get_all()
    return render_template("show_email.html", emails = all_emails)

