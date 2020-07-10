from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('header.html')
@app.route("/1")
def template_test1():
    return render_template('home1.html')
@app.route("/2")
def template_test2():
    return render_template('footer.html')


app.run(debug=True)
