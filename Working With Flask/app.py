from flask import Flask
'''
It creates an instance of the Flask class, which will be your WSGI application.
'''

# WSGI Application
app = Flask(__name__)

@app.route('/')
def home_page():
    return "Welcome to this Flask Course. This is the default/home page. You can go to the index page using the endpoint '/index'"

@app.route('/index')
def index():
    return "This is the index page"


if __name__=='__main__':
    app.run(debug=True,port=8080)