from flask import Flask, render_template, request, redirect, session
# added request and redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("survey.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    # session['username'] = request.form['name']
    # session['useremail'] = request.form['email']
    session['username'] = request.form['name']
    session['userplace'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomment'] = request.form['comment']
    return redirect('/result')
    # sends to the route of result

@app.route("/result")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")
    # prints out the result within the form

if __name__ == "__main__":
    app.run(debug=True)