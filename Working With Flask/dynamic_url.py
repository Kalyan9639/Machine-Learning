## In this session, we will learn about "Building URL dynamically"

from flask import Flask,render_template,request,redirect,url_for

# WSGI Application
app = Flask(__name__) 

@app.route('/')
def home_page():
    return """
    <html>
    <h1> Welcome to the Flask Course </h1>
    </html>
    """

@app.route('/result/<float:marks>')
def result(marks):
    res=""
    if marks>=50:
        res = "PASSED"
    else:
        res = 'FAILED'
    return render_template('results.html',results=res)

# Dynamic url
@app.route('/getresults',methods=['POST','GET'])
def get_results():
    total = 0
    if request.method == 'POST':
        s = float(request.form['science'])
        m = float(request.form['maths'])
        p = float(request.form['python'])
        ds = float(request.form['ds'])

        total = (s+m+p+ds)/4
    
        return redirect(url_for('result',marks=total))
   
    return render_template("get_results.html")


if __name__=='__main__':
    app.run(debug=True)
