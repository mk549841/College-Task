from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column,Integer,String

engine=create_engine('oracle://mk:1@localhost:1521/XE',echo=True)
Session = sessionmaker(bind=engine)
Base=declarative_base()

class Cse(Base):
    
    __tablename__="tbl_e"

    id=Column(Integer,primary_key=True)
    name=Column("Studentname",String(20))
         
    def __init__(self,id,name):
        self.id=id
        self.name = name
    def __repr__(self):
        return '{id:'+str(self.id)+', age:'+self.name+ '}'
      
   

Base.metadata.create_all(engine)
session=Session()

a1=Cse(3,"Vijay")
a2=Cse(2,"Ajith")
a3=Cse(1,"Mari")

#session.add_all([a1,a2,a3])
session.commit()

#qry=session.query(Cse).all()
#qry=session.query(Cse).filter_by(name='Vijay').all()
#qry=session.query(Cse).filter_by(name='Vijay').first()

qry=session.query(Cse).filter_by(name='Ajith').all()

print(qry)
