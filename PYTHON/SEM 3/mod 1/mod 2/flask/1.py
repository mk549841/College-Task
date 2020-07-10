from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('hello.html')

@app.route('/home')
def main1():
   return "<h1>Thank you for your responce<h1>"
if __name__ == '__main__':
   app.run(debug = True)

