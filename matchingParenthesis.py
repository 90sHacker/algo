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

def check_match(p1, p2):
  match = {
    '(': ')',
    '{': '}',
    '[': ']'
  }

  return match[p1] == p2

def is_balanced(data):
  stack = Stack()

  for ch in data:
    if ch == '(' or ch == '{' or ch == '[':
      stack.push(ch)

    if ch == ')' or ch == '}' or ch == ']':
      if stack.size() == 0:
        return False
      if not check_match(stack.pop(), ch):
        return False

  return stack.size() == 0


if __name__ == '__main__':
  print(is_balanced('({a+b})'))
  print(is_balanced("))((a+b}{"))
  print(is_balanced("((a+b))"))
  print(is_balanced("((a+g))"))
  print(is_balanced("))"))
  print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

