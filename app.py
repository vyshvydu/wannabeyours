# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Vyshnavi Vasanth"   
    age = "15" 

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/")
def index():

    name = "Vyshnavi Vasanth"  
    age = "15"  

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Sibi Vasanthan "#    "
    age = "41" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/father")
def home():

    name = "Vasanthan kS" # 
    age = "54" #  

    return render_template('father.html' , name = name , age = age)

# add other routes, if you want

@app.route("/friends")
def home():

    name = "Glona gitanjali" # write your name
    age = "32" # write your age

    return render_template('friends.html' , name = name , age = age)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
