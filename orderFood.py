from collections import deque
from threading import Thread
import time

class Queue:
  def __init__(self) -> None:
    self.buffer = deque()

  def enqueue(self, item):
    self.buffer.appendleft(item)

  def dequeue(self):
    return self.buffer.pop() 

  def size(self):
    return len(self.buffer)

  def is_empty(self):
    return len(self.buffer) == 0

queue = Queue()

def place_order(orders):
  for order in orders:
    queue.enqueue(order)
    time.sleep(0.5)
    
def serve_order():
  while queue.size() != 0:
    print(queue.dequeue())
    time.sleep(2)

if __name__ == '__main__':
  orders = ['pizza','samosa','pasta','biryani','burger']

  #create threads
  t1 = Thread(target=place_order, args=(orders,))
  t2 = Thread(target=serve_order)

  t1.start()
  time.sleep(1)
  t2.start()

  t1.join()
  t2.join()