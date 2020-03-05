import threading
from random import randint
import time


class Worker():
    def __init__(self, noOfThreads):
        self.noOfThreads = noOfThreads
        self.threads = []
        self.tasks = []
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)
        self.runThreads = True;
        self.__create()
       
    def acquire_job(self):
        while(self.runThreads):
            self.lock.acquire()
         
            if(len(self.tasks) == 0):
                self.cv.wait()
                
            #print("hello from thread", threading.get_ident()) this shows that threads are working
            if(len(self.tasks) != 0):
                localTask = self.tasks.pop(0)

            self.lock.release()
            localTask()

    def start(self):
        for i in range(0, len(self.threads)):
            self.threads[i].start()

    def post(self, task):
        self.lock.acquire()
        self.tasks.append(task)
        try:
            self.cv.notify(1)
        except RuntimeError:
            print("lock not aqquired")
        finally: 
            self.lock.release()
        

    def __create(self):
        for x in range(0, self.noOfThreads):
            self.threads.append(threading.Thread(target=self.acquire_job))
        print("added", self.noOfThreads, "threads")

        
    def stop(self):
        self.runThreads = False
            






def test():
    print("Random distance ", randint(2,40),"cm")

def test2():
    print("Random message, other function")

if __name__ == "__main__":
    workers = Worker(4)
    workers.start()
    
    #Testing breakpoints in worker system
    for x in range(0, 100):
        workers.post(test)
        if x > 50:
            time.sleep(1)
        if x%2 == 0:
            workers.post(test2)
   

    

    

