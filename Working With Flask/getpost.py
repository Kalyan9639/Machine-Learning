from flask import Flask,render_template,request

# WSGI Application
app = Flask(__name__) 

@app.route('/')
def home_page():
    return """
    <html>
    <h1> Welcome to the Flask Course </h1>
    </html>
    """

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Thank you {name}! You have registered to the course"
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True,port=8080)