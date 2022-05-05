class Node:
    def __init__(self, previous, value, next):
        self.previous = previous
        self.value = value    
        self.next = next        
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.next == other.next
        )
    def __repr__(self):
        return ("Node({!r}, {!r}, {!r})".format(self.previous, self.value, self.next))

class OrderedList:
    def __init__(self):
        '''Ititializes the ordered list'''
        self.head = None
        self.tail = None
        self.num_items = 0
    
    def __eq__(self, other):
        '''Tests equality between two ordered lists'''
        return (type(self) == type(other) == OrderedList) \
            and (self.num_items == other.num_items) \
            and (self.get_items() == other.get_items())   
    
    def __repr__(self):
        '''Format ordered list string representation'''
        return ("Ordered List: {!r}".format(self.get_items()))
    
    def get_items(self) -> list:
        '''Return a list of items in OrderedList'''
        items = []
        if self.num_items == 0:
            return items
        else:
            current = self.head
            while current != None:
                items.append(current.value)
                current = current.next
        return items
    
    def add(self, item: int) -> None:
        '''Adds item into list, preserving order'''
        current = self.head
        prev = None
        stop = False
        while not stop and current != None:
            if current.value > item:
                stop = True
            else: 
                prev = current
                current = current.next
        
        newNode = Node(None, item, None)
        if prev == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                temp = self.head
                self.head = newNode
                self.head.next = temp
                temp.previous = newNode
        else:
            temp = prev.next
            prev.next = newNode
            newNode.previous = prev
            newNode.next = temp
            if temp != None:
                temp.previous = newNode
            if current == None:
                self.tail = newNode
        self.num_items = self.num_items + 1
        
    def remove(self, item: int) -> None:
        '''Removes specified item from list'''
        current = self.head
        prev = None
        stop = False
        while not stop and current != None:
            if current.value == item:
                stop = True
            else: 
                prev = current
                current = current.next
        
        if prev == None:
            if current.next == None:
                current = self.head = self.tail = None
            else:
                current = current.next
                current.previous = None
                self.head = current
        else:
            if current.next == None:
                prev.next = None
                self.tail = prev
            else:
                next = current.next
                prev.next = next
                next.previous = prev
            
        self.num_items = self.num_items - 1
    
    def search_forward(self, item: int) -> bool:
        '''Starts at head node and moves forward, looking for given item'''
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.value == item:
                found = True
            else:
                if current.value > item:
                    stop = True
                else:
                    current = current.next
        return found
        
    def search_backward(self, item: int) -> bool:
        '''Starts at tail node and moves backward, looking for given item'''
        current = self.tail
        while current != None:
            if current.value == item:
                return True
            elif current.value < item:
                return False
            else:
                current = current.previous
        return False
    
    def is_empty(self) -> bool:
        '''Evaluates nodelist empty or not empty'''
        return self.head == None
    
    def size(self) -> int:
        '''Returns number of items in node list'''
        return self.num_items
    
    def index(self, item: int) -> int:
        '''Returns position of given item in list'''
        valueList = self.get_items()
        for idx in range(len(valueList)):
            if valueList[idx] == item:
                return idx
        return -1
    
    def pop(self, pos = -1) -> int:
        '''Removes and returns the last item in the list (unless position is specified)'''
        if pos == -1:
            item = self.tail.value
            if self.num_items > 1:
                prev = self.tail.previous
                prev.next = None
                self.tail = prev
            else:
                self.head = None
                self.tail = None
        else:
            if pos <= self.num_items / 2:
                current_idx = 0
                current = self.head
                while current_idx != pos:
                    current = current.next
                    current_idx = current_idx + 1
                item = current.value     
            else: 
                current_idx = self.num_items - 1
                current = self.tail
                while current_idx != pos:
                    current = current.previous
                    current_idx = current_idx - 1
                item = current.value
            if current == self.head:
                self.head = self.head.next
            elif current == self.tail:
                    prev = current.previous
                    prev.next = None   
            else:
                prev = current.previous
                next = current.next
                prev.next = next
                next.previous = prev 
        self.num_items = self.num_items - 1
        return item