from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column,Integer,String, Sequence,Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref

engine=create_engine('oracle://system:admin@localhost:1521/XE',echo=True)
Session = sessionmaker(bind=engine)
Base=declarative_base()

author_book_association = Table('authors_books', Base.metadata,
    Column('author_id', Integer, ForeignKey('tbl_authors.id')),
    Column('book_id', Integer, ForeignKey('tbl_books.id'))
)

class Author(Base):
    __tablename__ = "tbl_authors"
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True) 
    name = Column(String(50))  
    book = relationship("Book", secondary=author_book_association, back_populates="author")

class Book(Base):
    __tablename__ = "tbl_books"
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True) 
    name = Column(String(50))                                    
    author_id = Column(Integer, ForeignKey('tbl_authors.id'))              
    author = relationship("Author",secondary=author_book_association, back_populates="book")   

Base.metadata.create_all(engine)
session = Session()
author1 = Author(name="Agatha Christe")
author2 = Author(name="Dan Brown")
book1 = Book(name="And Then There Were None", author=[author1, author2])
book2 = Book(name="Destination Unknown", author=[author1, author2])
session.add(book1)
session.add(book2)
session.commit()
