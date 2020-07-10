import cx_Oracle
con=cx_Oracle.connect("mk/123@127.0.0.1/XE")
cur=con.cursor()
#cur.execute("""drop table mk""")
cur.execute("""create table mk (Id number,First_name varchar(100),Last_Name varchar(100),Email varchar(200),Year_of_born Number)""")
for i in range(int(input("Enter How Records in interger"))):
    det=[(int(input("Enter your id")),input("ENter your first name"),input("ENter your last name"),input("ENter your Email"),int(input("ENter your dob")))]
    cur.executemany("""insert into mk values(:1,:2,:3,:4,:5)""",det)
con.commit()
cur.execute("""select * from mk WHERE Year_of_born=1993""")
for i in cur.fetchall():
    print(i)
con.commit()
cur.execute("""Delete from mk where id=12""")
cur.execute("""select * from mk """)
for i in cur.fetchall():
    print(i)
print("Table Dropped")
cur.execute("""select * from mk """)
print("Now Table contains")
print(cur.fetchall())
cur.execute("""drop table mk""")
con.close()
