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
    __tablename__ = "tbl_author"
    id = Column(Integer, 
        Sequence('author_id_seq'), primary_key=True) 
    name = Column(String(50))  
    book = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "tbl_book"
    id = Column(Integer, 
        Sequence('book_id_seq'), primary_key=True) 
    name = Column(String(50))                                    
    author_id = Column(Integer,
                     ForeignKey('tbl_author.id'))              
    author = relationship("Author", back_populates="book")  

Base.metadata.create_all(engine)
session = Session()
book1 = Book(name="Core Python Programming")
book2 = Book(name="PYTHON THE COMPLETE REFERENCE ")
author1 = Author(name="Martin C. Brown",book=[book1,book2])
session.add(book1)
session.commit()
