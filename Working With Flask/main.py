# Integrating HTML with the Flask Web App

from flask import Flask,render_template

# WSGI Application
app = Flask(__name__) # It creates an instance of the Flask class, which will be your WSGI application.

@app.route('/')
def home_page():
    return """
    <html>
    <h1> Welcome to the Flask Course </h1>
    <h3> You can navigate to the index page using '/index' endpoint or by just clicking the below link </h3>
    <a href="http://127.0.0.1:8080/index"> Index Page </a>
    </html>
    """

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True,port=8080)