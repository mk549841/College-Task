from flask import Flask, jsonify,render_template
import math
app = Flask(__name__)
@app.route('/fact/<int:num>')
def fact(num):
    return f"<p align='center'>Factorial of <b>{num}</b> is <b>{math.factorial(num)}</b>........</p>"
@app.route('/multip/<int:num>')
def mul(num):
    return render_template('multi.html',num=num)
@app.route('/json')
def json():
    actors = [{'name': 'George Clooney', 'birthdate': '1961-05-06'},{'name': 'Salma Hayek', 'birthdate': '1967-09-02'},{'name': 'Jennifer Lopez', 'birthdate': '1969-07-24'},{'name': 'Colin Firth', 'birthdate': '1960-09-10'}]
    return jsonify(actors)
@app.route('/table')
def table():
    actors = [{'name': 'George Clooney', 'birthdate': '1961-05-06'},{'name': 'Salma Hayek', 'birthdate': '1967-09-02'},{'name': 'Jennifer Lopez', 'birthdate': '1969-07-24'},{'name': 'Colin Firth', 'birthdate': '1960-09-10'}]
    return render_template('tab.html',actors=actors)
if __name__ == "__main__":
    app.run(debug=True)
