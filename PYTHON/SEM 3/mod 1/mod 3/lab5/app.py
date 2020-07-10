from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='oracle://mk:1@localhost:1521/XE'
db=SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books_tbl'
    id =db.Column(db.Integer,db.Sequence('seq_book',start=1001),primary_key=True)
    title=db.Column(db.String(25))
    price=db.Column(db.Float)
    author=db.relationship("Author",back_populates='book')
    
    def __repr__(self):
        return f"<Book(title={self.title},price=Rs.{self.price},author={self.author})>"

class Author(db.Model):
    __tablename__='authors_tbl'
    id = db.Column(db.Integer,db.Sequence('seq_author',start=5001),primary_key=True)
    name=db.Column(db.String(20))
    bookid = db.Column(db.Integer,db.ForeignKey('books_tbl.id'))
    book = db.relationship("Book",back_populates='author')

    def __repr__(self):
        return f"<Author(name={self.name})>"

@app.route('/')
@app.route('/book',methods=['GET','POST'])
def book_store():
    if request.method=='GET':
        return render_template('bookstore.html')
    elif request.method=='POST':
        title=request.form['title']
        author_name=request.form['author']
        price=request.form['price']
        option=request.form['option']
        
        if option=='Add':
            author=Author(name=author_name)
            book=Book(title=title,author=[author],price=price)
            db.session.add(book)
            db.session.commit()
            
        elif option=='Update':
            book=Book.query.filter(Book.title==title).one()
            book.price=price
            db.session.commit()
            
        elif option=='Delete':
            book=Book.query.filter(Book.title==title).one()
            db.session.delete(book)
            db.session.commit()

        else:
            books=Book.query.all()
            return render_template('show.html',books=books)

        return render_template('bookstore.html')
    
if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
