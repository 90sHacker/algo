class TreeNode():
  def __init__(self, data) -> None:
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0
    #get level by counting parents
    p = self
    while p.parent:
      level += 1
      p = p.parent

    return level
  
  def print_tree(self):
    spaces = ' ' * self.get_level() * 3
    prefix = spaces + '|--' if self.parent else "" 
    
    print(prefix + self.data)

    if self.children:
      for child in self.children:
        child.print_tree()

def build_tree():
  root = TreeNode("Electronics")

  laptops = TreeNode('Laptops')
  laptops.add_child(TreeNode('Thinkpad'))
  laptops.add_child(TreeNode('Surface'))
  laptops.add_child(TreeNode('Mac'))

  phones = TreeNode('Phones')
  phones.add_child(TreeNode('Pixel'))
  phones.add_child(TreeNode('iPhone'))
  phones.add_child(TreeNode('Infinix'))

  tv = TreeNode('TVs')
  tv.add_child(TreeNode('LG'))
  tv.add_child(TreeNode('Samsung'))

  root.add_child(laptops)
  root.add_child(phones)
  root.add_child(tv)

  print(root.get_level())

  return root


if __name__ == '__main__':
  root = build_tree()
  root.print_tree()

