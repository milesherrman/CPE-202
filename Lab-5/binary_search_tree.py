class TreeNode: 
    '''data for node, references'''
    def __init__(self, key, lchild = None, rchild = None): 
        self.key = key 
        self.data = None
        self.left = lchild
        self.right = rchild 
        self.parent = None
        self.level = 0
        
    def __eq__(self,other):
        return (type(self) == type(other)) and \
            self.key == other.key
        
    def __repr__(self):
        return ("Node[{!r}]".format(self.key))
    
    def insert(self, newkey) -> None: 
        '''inserts a node with key into the correct position if not a duplicate. '''
        newNode = TreeNode(newkey)
        newNode.level = self.level + 1
        if self.key == newkey:
            newNode = None
        elif newkey < self.key:
            if self.left == None:
                self.left = newNode
                newNode.parent = self
            else:
                self.left.insert(newkey)
        else:
            if self.right == None:
                self.right = newNode
                newNode.parent = self
            else:
                self.right.insert(newkey)
    
    def find_successor(self): 
        '''returns the node that is the inorder successor of the node''' 
        if self.right != None:
            self = self.right
            while self.left != None:
                self = self.left
            return self
        else:
            return None
    
    def find_min(self) -> float: 
        '''returns the min value in the tree''' 
        if self.left == None:
            return self.key
        else:
            return self.left.find_min()
    
    def find_max(self) -> float: 
        '''returns max value in the tree'''
        if self.right == None:
            return self.key
        else:
            return self.right.find_max()
        
    def inorder_print_tree(self) -> None:   
        '''print inorder the subtree of self'''
        if self.left != None:
            self.left.inorder_print_tree()
        print(self.key, end = " ")
        if self.right != None:  
            self.right.inorder_print_tree()  
        
    def print_levels(self) -> None:
        '''inorder traversal prints list of pairs, [key, level of the node] where root is level 0'''
        if self.left != None:
            self.left.print_levels()
        print("[{!r}, {!r}]".format(self.key, self.level), end = " ")
        if self.right != None:  
            self.right.print_levels()
            
    '''Additional TreeNode methods below'''
    
    def is_root(self) -> bool:
        '''Returns True if node is root, else False'''
        return self.parent == None
    
    def is_leaf(self) -> bool:
        '''Returns True if node is a leaf, else False'''
        return self.left == None and self.right == None
    
    def is_left_child(self) -> bool:
        '''Returns True if node is a left child, else False'''
        parent = self.parent
        return parent.left == self
    
    def is_right_child(self) -> bool:
        '''Returns True if node is a right child, else False'''
        parent = self.parent
        return parent.right == self
    
    def search(self, key) -> bool:
        '''Returns True if TreeNode[key] is in subtree of self'''
        if self.key == None:
            return False
        elif self.key == key:
            return True
        elif self.key > key and self.left != None:
            return self.left.search(key)
        elif self.key < key and self.right != None:
            return self.right.search(key)
        else: 
            return False
        
    def find_node(self, key: float): 
        '''Returns node with given key''' 
        if self.key == key:
            return self
        elif self.key > key:
            return self.left.find_node(key)
        elif self.key < key:
            return self.right.find_node(key)
        
    def lower_level(self) -> None:
        '''Lowers  level of all nodes in the subtree of given TreeNode'''
        self.level = self.level - 1
        if self.left != None:
            self.left.lower_level()
        if self.right != None:
            self.right.lower_level()
    
    
    
class BinarySearchTree: 

    def __init__(self):
        self.root = None
        self.size = 0
        
    def __eq__(self,other):
        return (type(self) == type(other)) and \
            self.size == other.size and \
                self.root == other.root
        
    def __repr__(self):
        return ("Tree with {!r} nodes".format(self.size))
    
    def find(self, key: float) -> bool: 
        '''returns True if key is in a node of the tree, else False''' 
        if self.root == None:
            return False
        else:
            if self.root.key == key:
                return True
            elif self.root.key > key and self.root.left != None:
                return self.root.left.search(key)
            elif self.root.key < key and self.root.right != None:
                return self.root.right.search(key)
            else:
                return False
            
    def insert(self, newkey: float) -> None: 
        '''inserts a node with key into the correct position if not a duplicate. '''
        if self.root == None:
            self.root = TreeNode(newkey)
            self.size = self.size + 1
        else:
            if self.find(newkey) == False:
                self.root.insert(newkey)
                self.size = self.size + 1
    
    def delete(self, key: float) -> None:
        '''Deletes the node containing given key'''
        node = self.root.find_node(key)
        self.size = self.size - 1
        if self.size == 1:
            self.root = None
            self.size = 0

        elif node.is_leaf():
            parent = node.parent
            if node.is_left_child():
                parent.left = None
            elif node.is_right_child():
                parent.right = None
               
        elif node.right != None and node.left != None:
            next = node.find_successor()
            node.key = next.key
            node.data = next.data
            if next.is_leaf():
                if next.is_left_child():
                    next.parent.left = None
                elif next.is_right_child():
                    next.parent.right = None
            else:
                if next.is_left_child():
                    next.parent.left = next.right
                    next.right.lower_level()
                    next.right.parent = next.parent
                elif next.is_right_child():
                    next.parent.right = next.right
                    next.right.lower_level()
                    next.right.parent = next.parent
        
        else:
            if node.parent == self.root:
                self.root = node
                self.root.lower_level()    
            elif node.parent.left == node:
                if node.left != None:
                    node.left.lower_level()
                    node.left.parent = node.parent
                    node.parent.left = node.left
                else: 
                    node.right.lower_level()
                    node.right.parent = node.parent
                    node.parent.left = node.right
            elif node.parent.right == node:
                if node.left!= None:
                    node.left.lower_level()
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.right.lower_level()
                    node.right.parent = node.parent
                    node.parent.right = node.right
        
    def print_tree(self) -> None:
        '''print inorder the entire tree'''
        self.root.inorder_print_tree()
    
    def is_empty(self) -> bool:
        '''returns True if tree is empty, else False'''
        return self.size() == 0 
    