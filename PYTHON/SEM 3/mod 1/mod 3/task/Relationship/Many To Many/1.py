from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import exc
Base = declarative_base()

author_book_association = Table('authors_books', Base.metadata,
                                Column('author_id', Integer, ForeignKey('tbl_authors.id')),
                                Column('book_id', Integer, ForeignKey('tbl_books.id'))
                                )
class Author(Base):
    __tablename__ = "tbl_authors"
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    name = Column(String(50))
    book = relationship("Book", uselist=False, back_populates="author")


class Book(Base):
    __tablename__ = "tbl_books"
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    name = Column(String(50))
    author_id = Column(Integer, ForeignKey('tbl_authors.id'))
    author = relationship("Author", back_populates="book")
    
Session = sessionmaker()
engine=create_engine("oracle://mk:1@localhost:1521/XE")
Base.metadata.create_all(engine)
session = Session.configure(bind=engine)
session = Session()
author1 = Author(name="Agatha Christe")
author2 = Author(name="Dan Brown")
book1 = Book(name="And Then There Were None", author=author1)
book2 = Book(name="Destination Unknown", author=author1)
session.add(book1)
session.add(book2)
session.commit()
for u in session.query(Author).all():
    print(u.__dict__)
