from sqlalchemy.ext.declarative import *
from sqlalchemy import *
from sqlalchemy.orm import *

engine=create_engine("oracle://mk:1@localhost:1521/XE")

Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

session = Session()

class Vehicle(Base):
    __tablename__ = 'tbl_vehicle1'
    vehicle_id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(30))
    vehicle_type = Column(String(30))
    def __repr__(self):
        return f"vehicle_id={self.vehicle_id},vehicle_name={self.vehicle_name},type1={self.vehicle_type}>"


class TwoWheeler(Vehicle):
    __mapper_args__ = {
        'polymorphic_identity': '2-wheel'
        }



class FourWheeler(Vehicle):
    __mapper_args__ = {
        'polymorphic_identity': '4-wheel'
        }
    
bike = TwoWheeler(vehicle_id=101, vehicle_name='Honda')
session.add(bike)
car = FourWheeler(vehicle_id=102, vehicle_name='Honda')
session.add(car)
session.commit()


two = session.query(TwoWheeler).all()

four = session.query(FourWheeler).all()

for u in session.query(Vehicle).all():
    print(u.__dict__)
                  


