from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


# @app.route('/')
# def index():
#     return render_template("index.html", phrase="ryan", times=5)	# notice the 2 new named arguments!

@app.route('/play')
def box():
    return render_template("playground1.html")

@app.route('/play/<int:num>')
def multiply(num):
    num
    return render_template("playground2.html", times=num)
    
@app.route('/play/<int:num>/<color>')
def play(num, color):
    return render_template("playground3.html", times=num, color=color)
# This is the code for playground assignment




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    

    
# app.run(debug=True) should be the very last statement! 


# app.run(debug=True, host="localhost", port=8000)
