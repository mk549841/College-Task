from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column,Integer,String, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

engine=create_engine('oracle://system:admin@localhost:1521/XE',echo=True)
Session = sessionmaker(bind=engine)
Base=declarative_base()

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True) 
    name = Column(String(50))  
    book = relationship("Book", 
        uselist=False, back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,  primary_key=True) 
    name = Column(String(50))                                    
    author_id = Column(Integer, ForeignKey('authors.id'))              
    author = relationship("Author", back_populates="book") 

Base.metadata.create_all(engine)
session = Session()
author = Author(id=44431,name="A.P.J. Abdul Kalam")
book = Book(id=72,
name="Learning How to Fly: Life Lessons for the Youth",
author=author)
session.add(author)
session.add(book)
session.commit()
qry=session.query(Author).all()
print(qry)
