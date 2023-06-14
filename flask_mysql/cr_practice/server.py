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


@app.route("/user/update", methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route("/user/delete/<int:user_id>")
def delete(user_id):
    data = {"id": user_id}
    User.delete(data)
    return redirect ('/users')


if __name__ == "__main__":
    app.run(debug=True)

