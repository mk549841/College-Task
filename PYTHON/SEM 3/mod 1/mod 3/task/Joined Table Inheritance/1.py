from sqlalchemy.ext.declarative import *
from sqlalchemy import *
from sqlalchemy.orm import *

engine=create_engine("oracle://mk:1@localhost:1521/XE")

Session = sessionmaker()

Base = declarative_base()

Base.metadata.create_all(engine)

session = Session()

class Vehicle(Base):
    __tablename__ = 'tbl_vehicle'
    vehicle_id = Column(Integer,Sequence('veh_id',start=101) primary_key=True)
    vehicle_name = Column(String(30))
    vehicle_type = Column(String(30))
    __mapper_args__ = {
        'polymorphic_identity': 'vehicle',
        'polymorphic_on': vehicle_type
        }
    
class TwoWheeler(Vehicle):
    __tablename__ = 'tbl_two_wheeler'
    twid = Column(Integer, ForeignKey('tbl_vehicle.vehicle_id'),primary_key=True)
    model = Column(String(30))
    __mapper_args__ = {
        'polymorphic_identity': '2-wheel'
        }
    def __repr__(self):
        return f"vehicle_id={self.twid},vehicle_name={self.vehicle_name},model= {self.model}"
    
class FourWheeler(Vehicle):
    __tablename__ = 'tbl_four_wheeler'
    fwid = Column(Integer, ForeignKey( 'tbl_vehicle.vehicle_id'),primary_key=True)
    model = Column(String(30))
    __mapper_args__ = {
        'polymorphic_identity': '4-wheel'
        }
    def __repr__(self):
        return f"vehicle_id={self.fwid},vehicle_name={self.vehicle_name},model={self.model}"


bike = TwoWheeler(vehicle_id=101, vehicle_name='Honda', twid=101, model='Activa 4G')
session.add(bike)
car = FourWheeler(vehicle_id=102, vehicle_name='Honda', fwid=102, model='City')
session.add(car)
session.commit()

print(session.query(Vehicle).all())
two = session.query(TwoWheeler).all()
print(two)
four = session.query(FourWheeler).all()
print(four)




                  


