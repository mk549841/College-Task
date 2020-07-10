import cx_Oracle
con=cx_Oracle.connect("raja/raja@127.0.0.1/XE")
cur=con.cursor()
cur.execute("""drop table mk2""")
cur.execute("""create table mk2(emp_id  Number,emp_name  varchar(100),emp_designation  varchar(100),emp_address  varchar(100),emp_age number,emp_sal  number,emp_experience  number)""")
cur.execute("""create or replace procedure ins1(emp_id1 IN Number,emp_name1 IN varchar,emp_designation1 IN varchar,emp_address1 IN varchar,emp_age1 IN number,emp_sal1 IN number,emp_experience1 IN number)
is
begin
insert into mk2 values(emp_id1,emp_name1,emp_designation1,emp_address1,emp_age1,emp_sal1,emp_experience1);
end;
""")
cur.execute("""create or replace procedure ins
is
begin
update mk2 set emp_sal=1000 where emp_id=1;
end;
""")
cur.execute("""create or replace procedure ins2
is
begin
delete from  mk2 where emp_id=1;
end;
""")
cur.execute("""create or replace FUNCTION mukesh
return SYS_REFCURSOR
as
listall SYS_REFCURSOR;
begin
open listall for
    select *from mk2;
return listall;
end mukesh;
""")
for i in range(int(input("Enter How many records want to create"))):
    cur.callproc('ins1',[int(input("Enter your id")),input("Enter your name"),input("Enter designation"),input("Enter your address"),int(input("Enter your age")),int(input("Enter your salary")),int(input("Enter your Experience"))])
cur.callproc('ins')
cur.callproc('ins2')
my_c=cur.callfunc('mukesh',returnType=cx_Oracle.CURSOR)
con.commit()
print("Employees Details")
print('*'*30)
for i in my_c:
    print(i)
con.close()

