# a hash map uses key value pairs to store data
# a hash function uses a key to determine the hash in the index and stores the value at the location

class HashMap():
  
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
      return h % self.MAX
  
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    self.arr[h] = val

  def __getitem__(self, key):
    h = self.get_hash(key)
    return self.arr[h]

  def __delitem__(self, key):
    h = self.get_hash(key)
    self.arr[h] = None

    
if __name__ == '__main__':
  t = HashMap()
  t['oct'] = 90
  print(t.arr)
  print(t['oct'])
