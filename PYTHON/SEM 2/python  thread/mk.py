import threading
def fun(name):
    threading.current_thread().setName(name)
    print(threading.current_thread().getName())
t=threading.Thread(target=fun,args=('schooby',))
t1=threading.Thread(target=fun,args=('shaggy',))
t.start()
print('\n' )
t1.start()
