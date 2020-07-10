from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *

engine=create_engine("oracle://mk:1@localhost:1521/XE")

Session = sessionmaker()

session = Session.configure(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)



session = Session()

class Person(Base):
    __tablename__ = "tbl_persons"
    id = Column(Integer, Sequence('seq_person_id', start=101), primary_key=True)
    name = Column(String(25))
    age = Column(Integer)
    address = Column(String(35))
    email = Column(String(20))
# Constructor
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
# Getters
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_address(self):
        return self.address
    def get_email(self):
        return self.email
# Setters
    def set_name(self, value):
        self.name = value
    def set_age(self, value):
        self.age = value
    def set_address(self, value):
        self.address = value
    def set_email(self, value):
        self.email = value
    def __repr__(self):
        return f"name={self.get_name()},age={self.get_age()},address={self.get_address()},email={self.get_email()}"



obj=Person('mukesh',17,'tirunelveli','mk549841@gmail.com')
session.add(obj)
session.commit()
print(session.query(Person).all())



