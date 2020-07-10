import threading
import queue
class mk(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        r(self.name)
mk1=threading.Lock()

def r(x):
    mk1.acquire()
    print(x)
    mk1.release()
obj=queue.PriorityQueue()
#obj.put ( ( int(input("Enter the priority")),mk(input("enter student name"))))
obj.put((1,mk('ddhsdh')))
while not obj.empty():
    x=obj.get()[1]
    x.start()

