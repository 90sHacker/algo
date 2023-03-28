from collections import deque

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

if __name__ == '__main__':
  queue = Queue()
  queue.enqueue(5)
  queue.enqueue(5)
  queue.enqueue(5)
  print(queue.size())