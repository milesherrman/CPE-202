
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.cap = capacity
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                       # empty heap
        self.last_idx = 0

    def enqueue(self, item: int) -> None:
        """inserts "item" into the heap"""
        if not self.is_full():
            idx = self.last_idx + 1
            self.heap[idx] = item
            self.perc_up(idx)
            self.num_items = self.num_items + 1
            self.last_idx = self.last_idx + 1
        else:
            raise IndexError

    def peek(self) -> None:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if not self.is_empty():
            return self.heap[1]
        raise IndexError

    def dequeue(self) -> int:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if not self.is_empty():
            root = self.heap[1]
            last = self.heap[self.last_idx]
            self.heap[self.last_idx] = None
            self.heap[1] = last
            self.num_items = self.num_items - 1
            self.last_idx = self.last_idx - 1
            self.perc_down(1)  
            return root
        else:
            raise IndexError

    def contents(self) -> list:
        """returns a list of contents of the heap in the order it is stored"""
        heap_list = []
        for idx in range(1, self.num_items + 1):
            heap_list.append(self.heap[idx])
        return heap_list

    def build_heap(self, alist: list) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method."""
        if self.cap < len(alist):
            self.cap = self.num_items
        self.num_items = len(alist)
        self.last_idx = self.num_items
        self.heap = [None] + alist
        parent = self.size()//2
        while parent > 0:
            self.perc_down(parent)
            parent = parent - 1

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.cap

    def capacity(self) -> int:
        """Maximum number of a entries the heap can hold"""
        return self.cap
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i*2 > self.size():
            child1 = child2 = None
        elif i*2 + 1 > self.size():
            child1 = self.heap[2*i]
            child2 = None
        else:
            child1 = self.heap[2*i]
            child2 = self.heap[2*i + 1]
        if child1 != None:
            next = i*2
            if child2 != None and child2 > child1:
                    next = i*2 + 1
            if self.heap[i] < self.heap[next]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[next]
                    self.heap[next] = temp
                    self.perc_down(next)
                
    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i//2 != 0 and self.heap[i//2] < self.heap[i]:
                temp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = temp
                self.perc_up(i//2)
                
    def heap_sort_ascending(self, alist: list) -> list:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
            
        self.build_heap(alist)
        i = -1
        while self.num_items > 1:
            alist[i] = self.heap[1]
            i = i - 1
            self.heap[1],self.heap[self.num_items] = self.heap[self.num_items],self.heap[1]
            self.num_items = self.num_items - 1
            self.perc_down(1)
        alist[0] = self.heap[1]
        return alist