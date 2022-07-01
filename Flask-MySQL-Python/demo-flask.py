from flask import Flask, render_template#importing the module

app=Flask(__name__) #instantiating flask object

@app.route('/') #defining a route in the application
def func(): #writing a function to be executed 
       return 'Hey welcome to College'

# Pass the required route to the decorator.
@app.route("/hello")
def hellooo():
    return "Hello, Welcome to Flask Lesson..."
#app.add_url_rule('/hello', 'ccc',hellooo)

    
@app.route("/user")
def user():
    return "Homepage of testsite"


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    #return 'The about page'
    return render_template('about.html')


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"
       # return "Hello, "+ name
if __name__=='__main__': #calling  main 
       #app.debug=True #setting the debugging option for the application instance
       app.run() #launching the flask's integrated development webserver