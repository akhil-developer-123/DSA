class Queue:

  def __init__(self, capacity):
    self.size = 0
    self.capacity = capacity
    # frontend, rearend
    self.que = []

  def enqueue(self, value):
    if self.size == self.capacity:
      print("the queue is full. wait for space")
    else:
      self.que.insert(0, value)
      self.size = self.size + 1

  def dequeue(self):
    if self.size == 0:
      print("queue is empty. cannot deque")
    else:
      dequeuedElement = self.que.pop()
      print("dequeuing ", dequeuedElement)
      self.size -= 1


que1 = Queue(3)

que1.enqueue(10)
que1.enqueue(20)
que1.enqueue(30)
que1.enqueue(40)
que1.enqueue()

que1.dequeue()
que1.dequeue()
que1.dequeue()
que1.dequeue()
