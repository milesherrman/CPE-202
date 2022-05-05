# NodeList version of ADT Queue

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list

class Node:
    def __init__(self, value, rest):
        self.value = value      # value
        self.rest = rest        # NodeList
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Queue:
    def __init__(self):
        self.rear = None    # rear NodeList
        self.front = None   # front NodeList
        self.num_items = 0  # number of items in Queue

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.get_items() == other.get_items()
        )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    def get_items(self):
        '''Return list of items in queue'''
        items = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        return items

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise"""
        return self.num_items == 0

    def enqueue(self, item):
        """Adds item to the rear NodeList
        Must be O(1)"""
        newNode = Node(item, None)
        if self.is_empty():
            self.front = newNode
            self.rear = newNode
        else: 
            self.rear.rest = newNode
            self.rear = newNode
        self.num_items = self.num_items + 1
    
    def dequeue(self):
        """Returns and removes first item in the NodeList"""
        if self.size() == 0:
                raise IndexError
        else:
            temp = self.front.value
            self.front = self.front.rest
        self.num_items = self.num_items - 1
        if self.size() == 0:
            self.rear = None
        return temp
        
    def size(self):
        """Returns the number of items in the queue"""
        return self.num_items

if __name__ == "__main__":
    
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q2 = Queue()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q1 == q2)
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print("q1: ", q1)
    print("q2: ", q2)
    print(q1 == q2)
    q2.enqueue(4)
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    q2.enqueue(8)
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2)
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print("q1: ", q1)
    print("q2: ", q2)
    print(q2 == q1)
    