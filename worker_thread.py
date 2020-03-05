import threading

import time


class Worker():
    def __init__(self, noOfThreads):
        self.noOfThreads = noOfThreads
        self.threads = []
        self.tasks = []
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)
        self.runThreads = True;
       
    def acquire_job(self):
        while(self.runThreads):
            self.lock.acquire()
         
            if(len(self.tasks) == 0):
                self.cv.wait()
            
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
        

    def run(self):
        for x in range(0, self.noOfThreads):
            self.threads.append(threading.Thread(target=self.acquire_job))
            print("added thread", x)

        
    def stop(self):
        self.runThreads = False

            






def test():
    print("Lol")

if __name__ == "__main__":
    workers = Worker(4)
    workers.run()
    workers.start()
    workers.post(test)
    time.sleep(2)
    workers.stop()
    workers.post(test)

    

    

