from collections import deque

class Stack:
  def __init__(self) -> None:
    self.stack = deque()

  def push(self, item):
    self.stack.append(item)

  def print(self):
    print(self.stack)

  def pop(self):
    return self.stack.pop()
  
  def size(self):
    return len(self.stack)

  def peek(self):
    return self.stack[-1]

  def is_empty(self):
    return len(self.stack) == 0

  def batch_push(self, data):
    for d in data:
      self.stack.append(d)

if __name__ == '__main__':
  stack = Stack()
  stack.batch_push('We will conquer COVID-19')
  rstr = ''
  for i in range(stack.size()):
    rstr += stack.pop()

  print(rstr)
