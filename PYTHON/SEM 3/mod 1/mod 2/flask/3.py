from flask import *  
app = Flask(__name__)  
app.secret_key = "mukesh"  
     
@app.route('/')  
def home():  
    return render_template("home.html")  
     
@app.route('/login')  
def login():  
    return render_template("login.html")  
 
@app.route('/success',methods = ["POST"])  
def success():  
    if request.method == "POST":  
        session['name1']=request.form['name1']
        session['age']=request.form['age']
        session['email']=request.form['email']
        session['pn']=request.form['pn']
        session['pa']=request.form['pa']
        return render_template('success.html')  
@app.route('/profile')  
def profile():
    name1=session['name1']
    age=session['age']
    email=session['email']
    pn=session['pn']
    pa=session['pa']
    return  render_template('profile.html',a=name1,b=age,c=email,d=pn,e=pa)  
      
if __name__ == '__main__':  
    app.run(debug = True)  
