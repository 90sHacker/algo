class Node:
  def __init__(self, item) -> None:
    self.item = item
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None

  def insert_at_beginning(self, item):
    node = Node(item)
    node.next = self.head

    self.head = node


  def insert_at_end(self, item):
    if self.head is None:
      self.head = Node(item)
      return

    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(item)

  def print(self):
    if self.head is None:
      print('Linked List is empty')

    itr = self.head #new pointer
    lstr = ""
    while itr:
      lstr += str(itr.item) + '--->'
      itr = itr.next

    print(lstr)
  
  def insert_values(self, data):
    for d in data:
      self.insert_at_end(d)

  def get_length(self):
    count = 0

    itr = self.head
    while itr:
      count += 1
      itr = itr.next

    return count

  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      raise Exception('Index is out of bounds')

    if index == 0:
      self.head = self.head.next
      return

    count = 0
    itr = self.head
    while itr:
      count += 1
      if count == index:
        itr.next = itr.next.next
        break
      itr = itr.next
  
  def insert_at(self, index, item):
    if index < 0 or index >= self.get_length():
      raise Exception('Invalid Index')

    if index == 0:
      self.insert_at_beginning(item)
      return
    
    count = 0
    itr = self.head
    while itr:
      count += 1
      if count == index:
        node = Node(item)
        node.next = itr.next
        itr.next = node
        break
      itr = itr.next

  def insert_after_value(self, item_after, item_to_insert):
    # Search for first occurance of item_after value in linked list
    if self.head is None:
      return

    if self.head.item == item_after:
      node = Node(item_to_insert)
      node.next = self.head.next
      self.head.next = node
      return

    itr = self.head
    while itr:
      if itr.item == item_after:
    # Now insert item_to_insert after item_after node
        node = Node(item_to_insert)
        node.next = itr.next
        itr.next = node
        break
      itr = itr.next
  
  def remove_by_value(self, item):
    #Remove first occurrence of item
    if self.head is None:
      return

    if self.head.item == item:
      #self.remove_at(0)
      self.head = self.head.next
      return

    itr = self.head
    while itr.next:
      if itr.next.item == item:
        itr.next = itr.next.next
        break
      itr = itr.next
  

if __name__ == '__main__':
  list = LinkedList()
  list.insert_at_beginning(3)
  list.insert_at_beginning(2)
  list.insert_at_end(4)
  list.insert_at_beginning(1)
  list.insert_at_beginning(0)
  list.print()
  list.insert_values([5,6,7,8])
  list.print()
  print(list.get_length())
  list.remove_at(5)
  list.print()
  list.insert_at(5, 5)
  list.insert_after_value(8,10)
  list.insert_after_value(20,9)
  list.print()

  ll = LinkedList()
  ll.insert_values(["banana","mango","grapes","orange"])
  ll.print()
  ll.insert_after_value("banana","apple") # insert apple after mango
  ll.print()
  ll.remove_by_value("orange") # remove orange from linked list
  ll.print()
  ll.remove_by_value("figs")
  ll.print()
  ll.remove_by_value("banana")
  ll.remove_by_value("mango")
  ll.remove_by_value("apple")
  ll.remove_by_value("grapes")
  ll.print()


      

