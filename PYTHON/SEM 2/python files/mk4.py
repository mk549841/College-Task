try:
    class Employee:
        def __init__(self,name,dob,dept,des,salary):
            self.__name=name
            self.__dob=dob
            self.__dept=dept
            self.__des=des
            self.__salary=salary
        def get_name(self):
            return self.__name
        def get_dob(self):
            return self.__dob
        def get_dept(self):
            return self.__dept
        def get_des(self):
            return self.__des
        def get_salary(self):
            return self.__salary
        def set_name(self, value):
            self.__name = value
        def set_dob(self, value):
            self.__dob = value
        def set_dept(self, value):
            self.__dept = value
        def set_desn(self, value):
            self.__des = value
        def set_sal(self, value):
            self.__salary = value
    import pickle
    with open("input",'wb') as fp:
        obj=Employee(input("Enter the name "),input("Enter the DOB "),input("Enter the Department "),input("Enter the Designation "),input("Enter the Salary "))
        pickle.dump(obj,fp)
    with open("input","rb") as fp1:
        obj1=pickle.load(fp1)
        print('Name :',obj1.get_name())
        print("DOB :",obj1.get_dob())
        print("Designation :",obj1.get_des())
        print("Department :",obj1.get_dept())
        print('Salary :',obj1.get_salary())
except Exception as e:
    print(e)
