from sqlalchemy.engine import create_engine 

engine=create_engine('oracle://mk:1@localhost:1521/XE',echo=True)

# Create connection
conn = engine.connect()
#conn.execute('create table  bala(name varchar2(25))')
conn.execute('''insert into bala values('Ranjith')''')
# Close connection
conn.close()
