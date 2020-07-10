from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import exc

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "tbl_authors"
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    name = Column(String(50))
    book = relationship("Course", back_populates="author")


class Course(Base):
    __tablename__ = "tbl_books"
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    name = Column(String(50))
    author_id = Column(Integer, ForeignKey('tbl_authors.id'))
    author = relationship("Teacher", back_populates="book")
    def __repr__(self):
        return f"<Name={self.name},Course_id= {self.author_id}"



Session = sessionmaker()
engine=create_engine("oracle://mk:1@localhost:1521/XE")
Base.metadata.create_all(engine)
session = Session.configure(bind=engine)
session = Session()

author1 = Teacher(name="Agatha Christe")
book1 = Course(name="Mukesh",author=author1)
session.add(book1)
session.commit()


#print(session.query(Author).all())
print(session.query(Course).all())





                  


