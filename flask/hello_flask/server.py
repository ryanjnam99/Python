from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/')
def index():
    return render_template("index.html", phrase="ryan", times=5)	# notice the 2 new named arguments!

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

# @app.route('/<int:num>/<int:num2>/<string:one>/<string:two>')
# def checkerboard(num,num2,one,two):
#     return render_template("checkerboard.html", row=num, column=num2, color=one, color2=two)
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def row_col_two(x,y,color1,color2):
    return render_template("checkerboard.html",row=x,col=y,color_one=color1,color_two=color2)
    
# @app.route('/success')
# def success():
#   return "success"
    
# # app.run(debug=True) should be the very last statement! 

# @app.route('/dojo')
# def dojo():
#     return "Dojo!"

# @app.route('/hi/<name>')
# def hi(name):
#     print(name)
#     return f"Hi {str.capitalize(name)}!"

# @app.route('/repeat/<name>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def repeat(name, num):
#     print(name)
#     return f"{name * num}"

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"{word}\n"

#     return output

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    
\
    
# app.run(debug=True) should be the very last statement! 


# app.run(debug=True, host="localhost", port=8000)
