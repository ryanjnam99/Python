from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user_model import User


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

@app.route('/user/show/<int:user_id>')
def show(user_id):
    data ={ 
        "id":user_id
    }
    one_user = User.get_one(data)
    return render_template("show.html",user=one_user)

    
@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    data ={ 
        "id":user_id
    }
    one_user = User.get_one(data)
    return render_template("edit_user.html",user=one_user)


@app.route("/user/update/<int:user_id>", methods=['POST'])
def update(user_id):
    User.update(request.form)
    return redirect('/users')

@app.route("/user/delete/<int:user_id>")
def delete(user_id):
    data = {"id": user_id}
    User.delete(data)
    return redirect ('/users')
