import cx_Oracle
con=cx_Oracle.connect("m6/1@127.0.0.1/XE")
cur=con.cursor()
cur.execute("""drop table mk2""")
cur.execute("""create table mk2(train_id  Number,train_name  varchar(100),From_address  varchar(100),To_adddress  varchar(100),dep varchar(100),arrival varchar(100),train_class  varchar(100))""")
cur.execute("""create or replace procedure ins1(id IN Number,name1 IN varchar,From_ IN varchar,To_ IN varchar,dep1 IN varchar,arr  IN varchar,class_ IN varchar)
is
begin
insert into mk2 values(id,name1,From_,To_,dep1,arr,class_);
end;
""")
'''cur.execute("""create or replace procedure ins
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
""")'''
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
for i in range(int(input("Enter How many train records want to create"))):
    cur.callproc('ins1',[int(input("Enter train id")),input("Enter train name"),input("Enter From address"),input("Enter to address"),input("Enter desnitation"),input("Enter arrival"),input("Enter train class")])
#cur.callproc('ins')
#cur.callproc('ins2')
my_c=cur.callfunc('mukesh',returnType=cx_Oracle.CURSOR)
con.commit()
print("Train  Details")
print('*'*120)
for i in my_c:
    print(i)
con.close()

