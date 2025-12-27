## In this session, we will learn: 
### Variable rule
### Jinja 2 Template Engine

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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Thank you {name}! You have registered to the course"
    return render_template('form.html')

# variable rule
# Use 'int' converter for numeric scores
@app.route('/success/<int:score>')
def success(score):
    return "The marks you scored is: " + str(score)

@app.route('/result/<int:marks>')
def result(marks):
    res=""
    if marks>=50:
        res = "PASSED"
    else:
        res = 'FAILED'
    return render_template('results.html',results=res)

@app.route('/success_results/<int:marks>')
def final_results(marks):
    res=""
    if marks>=50:
        res = "PASSED"
    else:
        res = 'FAILED'

    exp = {'score':marks,'result':res}
    return render_template('result1.html',results=exp)

if __name__=='__main__':
    # print(app.url_map)
    app.run(debug=True)
