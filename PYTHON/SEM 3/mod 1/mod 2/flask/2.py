from flask import Flask  
app = Flask(__name__)    
@app.route('/')   
def hello():
    return 'Good Morning !'
@app.route('/hello/<name>')
def hello1(name):
    return '<h1>Good Morning! %s</h1>' %name

if __name__ == '__main__':  
    app.run(debug=True)
