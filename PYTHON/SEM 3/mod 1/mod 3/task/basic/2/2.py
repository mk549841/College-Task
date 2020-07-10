from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
Session = sessionmaker()
engine=create_engine("oracle://mk:1@localhost:1521/XE")


Session.configure(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)

session = Session()




class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, Sequence( 'product_id_seq',start=101),primary_key=True)
    title = Column(String(25))
    in_stock = Column(Boolean)
    quantity = Column(Integer)
    price = Column(Numeric)



pen = Product(title="pen", quantity=10, price=25.00,in_stock=True)

laptop = Product(title="laptop", quantity=5, price=39699.00,in_stock=True)

session.add(pen)
session.add(laptop)
session.commit()
session.close()

qry=session.query(Product).all()
print(qry)

qry=session.query(Product).filter_by(title='laptop').first()
print(qry)
# select exactly one row
qry=session.query(Product).filter_by(title='laptop').one()
print(qry)
# select specific columns
qry=session.query(Product.product_id,Product.title).all()
print(qry)
# select specific rows
qry=session.query(Product).filter_by(title='laptop')
print(qry)





