import cx_Oracle
con=cx_Oracle.connect("raja/raja@127.0.0.1/XE")
cur=con.cursor()
cur.execute("""drop table mk""")
cur.execute("""create table mk (EX_Id number primary key,type_of_exercise varchar(100),minutes_of_doing_it number,calories_burn number,heart_beat_rate Number)""")
for i in range(int(input("Enter How Records in interger"))):
    det=[(int(input("EX_ID")),input("ENter exercise name"),int(input("mins")),int(input("calories burn")),int(input("ENter heart beat rate")))]
    cur.executemany("""insert into mk values(:1,:2,:3,:4,:5)""",det)
con.commit()

cur.execute("""select *from mk where calories_burn >50 and minutes_of_doing_it>30""")
for i in cur.fetchall():
    print(i)
    cur.execute("""select *from mk where calories_burn>50 and heart_beat_rate>100""")
for i in cur.fetchall():
    print(i)
cur.execute("""select *from mk where calories_burn>50""")
for i in cur.fetchall():
    print(i)
con.close()
