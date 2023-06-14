from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route('/')
def index():
    # calling the get_all method from the friends.py
    all_friends=Friend.get_all()
    # passing all friends to our template so we can display them there
    return render_template("index.html",friends=all_friends)
@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html",friend=friend)


# relevant code snippet from server.py

@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')

# @app.route('/create_friend', methods=["POST"])
# def create_friend():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "occ" : request.form["occ"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     Friend.save(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)

