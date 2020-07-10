import threading
from time import sleep
from threading import Thread
class salesperson(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        print(self.name)
class days(threading.Thread):
    def __init__(self,day):
        threading.Thread.__init__(self)
        self.day=day
    def run(self):
        for i in self.day:
            if self.day in ['wednesday','Thursday','friday','saturday']:
                name=['mukesh','raja']
                for i in name:
                    t2=salesperson(i)
                    t2.start()
                    print("\nDay {}\n".format(self.day))
            
day=['sunday','monday','tuesday','wednesday','Thursday','friday','saturday']
for i in day:
    t2=days(i)
    t2.start()
    t2.join()
        
      
                
    
        
        
        
