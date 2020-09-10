import multiprocessing 
import time 

def test():
  print("sleeping for 1 sec")
  time.sleep(1)
  print("sleeping done"
  

p1 = multiprocessing.Process(target=test)

p1.start()

  
