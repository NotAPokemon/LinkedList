binary = ["0", "1"]


class LinkedList:

  def __init__(self, data, parent, id):
    self.child = None
    self.data = data
    self.parent = parent
    self.id = id

  def write(self, data, id):
    if id > 990:
      print("Error: ID is too large max 990")
      return None
    if self.id == id:
      print(self.id)
      self.data = data
    else:
      if self.child:
        self.child.write(data, id)
      else:
        if self.id == id - 1:
          self.child = LinkedList(data, self, id)
        else:
          self.child = LinkedList(None, self, self.id + 1)
          self.child.write(data, id)

  def read(self, id):
    if id == -1:
      len = self.len(0, "get")
      return len[1].data
    if self.id == id:
      return self.data
    else:
      if self.child:
        return self.child.read(id)
      else:
        return "Not found"

  def new(self, data):
    if self.child:
      self.child.new(data)
    else:
      self.child = LinkedList(data, self, self.id + 1)

  def len(self, run, *args):
    if self.child:
      return self.child.len(run + 1)
    else:
      if args[0] == "get":
        return run, self
      else:
        return run
class Tree:

  def __init__(self, data, parent, gen, id):
    self.left = None
    self.right = None
    self.data = data
    self.parent = parent
    self.gen = gen
    self.id = id

  def write(self, data, seq, run):
    try:
      x = seq[run]
      if x == "0":
        if self.left:
          return self.left.write(data, seq, run + 1)
        else:
          self.left = Tree(None, self, self.gen + 1, None)
          return self.left.write(data, seq, run + 1)
      elif x == "1":
        if self.right:
          return self.right.write(data, seq, run + 1)
        else:
          self.right = Tree(None, self, self.gen + 1, None)
          return self.right.write(data, seq, run + 1)
    except:
      self.data = data
      self.id = seq

  def read(self, seq, run):
    try:
      x = seq[run]
      if x == "0":
        if self.left:
          return self.left.read(seq, run + 1)
        else:
          return "Not found"
      elif x == "1":
        if self.right:
          return self.right.read(seq, run + 1)
        else:
          return "Not found"
    except:
      return self.data