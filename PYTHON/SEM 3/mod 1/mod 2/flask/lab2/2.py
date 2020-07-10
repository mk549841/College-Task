from flask import *  
app=Flask(__name__)

app.secret_key = "mukesh"
  
     
@app.route('/')  
def login():  
    return render_template("login.html")  
 
@app.route('/success',methods = ["POST"])  
def success():  
    if request.method == "POST":  
        session['name1']=request.form['name1']
        session['tele']=request.form['tele']
        session['email']=request.form['email']
        session['age']=request.form['age']
        session['gender']=request.form['gender']
        session['box']=request.form['box']
        return render_template('success.html')  
@app.route('/profile')  
def profile():
    name1=session['name1']
    tele=session['tele']
    email=session['email']
    age=session['age']
    gender=session['gender']
    box=session['box']
    
    return  render_template('indexpage.html',a=name1,b=tele,c=email,d=age,e=gender,f=box)  
if __name__ == '__main__':
    app.run(debug=True)
