class Frontier:
  def __init__(self):
    self.frontier = []

  def add(self,value):
    self.frontier.append(value)
  
  def remove(self):
    return self.frontier.pop()
    

class Stack(Frontier):
  def showStack(self):
    return self.frontier

class Queue(Frontier):
  def showQueue(self):
    return self.frontier
  def remove(self):
    x = self.frontier[0]
    if x:
      self.frontier.remove(self.frontier[0])
      return x
    else:
      raise IndexError()

x = Queue()
x.add(1)
x.add(4)
x.add(1)
x.add(4)

print(x.remove())
print(x.showQueue())