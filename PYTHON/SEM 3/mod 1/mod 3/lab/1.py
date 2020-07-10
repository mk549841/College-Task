from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import exc
Base = declarative_base()

class customer(Base):
    __tablename__ = "customers"
    cust_id = Column(Integer, Sequence('seq_cust_id', start=5001), primary_key=True)
    name = Column(String(25))
    address = Column(String(35))
    customer_type= Column(String(20))
# Constructor
    def __init__(self,cust_id,name,address,customer_type):
        self.cust_id=cust_id
        self.name = name
        self.address = address
        self.customer_type = customer_type
# Getters
    def get_id(self):
        return self.cust_id
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_type(self):
        return self.customer_type
# Setters
    def set_id(self, value):
        self.cust_id = value
    def set_name(self, value):
        self.name = value
    def set_address(self, value):
        self.address = value
    def set_type(self, value):
        self.customer_type = value
    def __repr__(self):
        return f"CUSTOMER ID = {self.get_id()}\nNAME = {self.get_name()}\nADDRESS = {self.get_address()}\nCUSTOMER TYPE = {self.get_type()}"



Session = sessionmaker()
engine=create_engine("oracle://mk:1@localhost:1521/XE")
Base.metadata.create_all(engine)
session = Session.configure(bind=engine)
session = Session()
li=[]
print('Enter Five id ')
for i in range(5):
    li.append(input())
li1=[]
print('Enter Five Name ')
for i in range(5):
    li1.append(input())
li2=[]
print('Enter Five address ')
for i in range(5):
    li2.append(input())
li3=[]
print('Enter Five Customer type ')
for i in range(5):
    li3.append(input())
obj=customer(li[0],li1[0],li2[0],li3[0])
obj1=customer(li[1],li1[1],li2[1],li3[1])
obj2=customer(li[2],li1[2],li2[2],li3[2])
obj3=customer(li[3],li1[3],li2[3],li3[3])
obj4=customer(li[4],li1[4],li2[4],li3[4])
session.add(obj)
session.add(obj1)
session.add(obj2)
session.add(obj3)
session.add(obj4)
session.commit()
#3
print('First Record')
print(session.query(customer).first())
session.commit()
print(session.query(customer).all())
#4
print('Update the address of any customer .')
session.query(customer).filter_by(name=li1[0]).update({customer.address:'Covai'})
session.commit()
qry=session.query(customer).all()
print(qry)

print('Display customerId, name and customerType of all the customers.')
qry=session.query(customer.cust_id,customer.name,customer.customer_type).all()
print(qry)
print("Delete any two person from the table  ")
session.query(customer).filter_by(name=li1[0]).delete()
session.query(customer).filter_by(name=li1[0]).delete()
session.commit()
qry=session.query(customer).all()
print(qry)
session.close()




