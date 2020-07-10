from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import exc

Base = declarative_base()


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
book1 = Book(name="And Then There Were None",author=author1)
session.add(book1)
session.commit()

def object_as_dict(book1):
    return {c.key: getattr(book1, c.key)
            for c in inspect(book1).mapper.column_attrs}

query = session.query(Book)
for user in query:
    print(object_as_dict(user))






                  



