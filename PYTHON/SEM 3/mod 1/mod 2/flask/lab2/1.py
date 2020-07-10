from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  
def home():  
    return render_template("home.html")  
     
@app.route('/name')
def name1():  
    return render_template("name.html")  
 
@app.route('/list')  
def list1():
        return render_template('list.html')  
@app.route('/image')  
def image1():
    return  render_template('img.html')
@app.route('/table')  
def table1():
    return  render_template('tab.html')
@app.route('/reg')  
def reg1():
    return  render_template('reg.html')
      
if __name__ == '__main__':  
    app.run(debug = True)  
