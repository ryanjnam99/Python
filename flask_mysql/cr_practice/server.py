from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def everyone():
    all_users = User.get_all()
    return render_template("users.html", users=all_users)

@app.route('/users/new')
def add():
    return render_template("add_user.html")

@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)

