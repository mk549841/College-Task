from app import db
from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='oracle://system:admin@localhost:1521/XE'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))
    date_created=db.Column(db.DateTime, default=datetime.now)

@app.route('/<name>/<address>')
def index(name,address):
    user=User(name=name,address=address)
    db.session.add(user)
    db.session.commit()
    
    return '<h1>Added new USER </h1>'

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
