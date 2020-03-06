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
            with self.lock: # might not work with release there also
                if(len(self.tasks) == 0):
                    self.cv.wait()
                    
                #print("hello from thread", threading.get_ident()) this shows that threads are working
                if(len(self.tasks) != 0):
                    localTask = self.tasks.pop(0)
                    self.lock.release()
                    localTask()
                else: 
                    self.lock.release()

            

    def start(self):
        for i in range(0, len(self.threads)):
            self.threads[i].start()

    def post(self, task):
        with self.lock: #run block of code and the releases lock
            self.tasks.append(task)
            try:
                self.cv.notify(1)
            except RuntimeError:
                print("lock not aqquired") #should never receive this exception hopefully
          
        

    def __create(self):
        for x in range(0, self.noOfThreads):
            self.threads.append(threading.Thread(target=self.acquire_job))
        print("added", self.noOfThreads, "threads")

        
    def stop(self):
        self.runThreads = False
            






    

    

