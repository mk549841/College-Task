from time import sleep
import threading
class example(threading.Thread):
    def __init__(self,name,rollnos):
        threading.Thread.__init__(self)
        self.name=name
        self.rollnos=rollnos
    def run(self):
        fun(self.name,self.rollnos)
mk=threading.Lock()

def fun(name,rollnos):
    mk.acquire()
    print("{}name {} Roll number started their presentation".format(name,rollnos))
    sleep(1)
    print("{}name {} Roll number End their presentation".format(name,rollnos))
    mk.release()
import queue
obj=queue.PriorityQueue()
li=[]
for i in range(int(input('Enter the count'))):
    obj.put ( ( int(input("Enter the priority")),example(input("enter student name"),int(input('Enter student rollnumber')))))

while not obj.empty():
    x=obj.get()[1]
    x.start()
    x.join()
