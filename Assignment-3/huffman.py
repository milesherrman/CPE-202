from xml.dom.minidom import CharacterData
import os

class HuffmanNode:
    def __init__(self, char_ascii = None, freq = None):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right
        self.parent = None
        
    def __repr__(self):
        return ("HNode({!r},{!r})".format(chr(self.char_ascii), self.freq))
    
    def __eq__(self, other):
        return (type(self) == type(other) == HuffmanNode) and \
            self.left == other.left and self.right == other.right and \
                self.freq == other.freq and self.char_ascii == other.char_ascii
    
    def __lt__(self, other):
        return comes_before(self, other) 

    def is_left(self):
        if self.parent != None:
            return self.parent.left == self
        return False
    
    def is_right(self):
        if self.parent != None:
            return self.parent.right == self
        return False
    
    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node
        
    def set_parent(self, node):
        self.parent = node
        
    def is_leaf(self):
        return self.left == None and self.right == None

def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if node a comes before node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        return a.char_ascii < b.char_ascii
    
def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    '''Creates and returns a new Huffman node with children a and b'''
    newNode = HuffmanNode()
    newNode.freq = a.freq + b.freq
    if comes_before(a,b):
        newNode.left = a
        newNode.right = b  
    else:
        newNode.left = b
        newNode.right = a
    if a.char_ascii < b.char_ascii:
        newNode.char_ascii = a.char_ascii
    else:
        newNode.char_ascii = b.char_ascii
    a.parent = newNode
    b.parent = newNode
    return newNode

def cnt_freq(filename: str) -> list:
    '''Opens file and returns list of character frequencies'''
    freq_list = [0]*256
    if os.stat(filename).st_size == 0:
        return freq_list
    huffman_input = open(filename, 'r', newline='')
    for line in huffman_input:
        for char in line:
            val = ord(char)
            freq_list[val] = freq_list[val] + 1
    huffman_input.close()
    return freq_list

def create_huff_tree(freq_list: list) -> HuffmanNode:
    '''Create a huffman tree and return the root node. Returns None if all counts are zero.'''
    huffman_list = []
    for idx in range(256):
        if freq_list[idx] != 0:
            huffman_list.append(HuffmanNode(idx, freq_list[idx]))
    if len(huffman_list) == 0:
        return None
    elif len(huffman_list) == 1:
        return huffman_list[0]
    else:
        huffman_list.sort(key = lambda x: (x.freq, x.char_ascii))
    while True:
        newNode = combine(huffman_list[0], huffman_list[1])
        if len(huffman_list) == 2:
            huffman_list = [newNode]
            break
        else:
            huffman_list = [newNode] + huffman_list[2:]
            huffman_list.sort(key = lambda x: (x.freq, x.char_ascii))
    return huffman_list[0]

def create_code(node: HuffmanNode) -> list:
    '''Returns a list of Huffman codes for every character in the tree'''
    code_list = [""]*256
    if node == None:
        return code_list
    elif node.is_leaf():
        code_list[node.char_ascii] = "0"
        return code_list
    curr_str = ""
    current = node
    while True:
        if current.left != None:
            current = current.left
            curr_str = curr_str + "0"
        elif current.right != None:
            current = current.right
            curr_str = curr_str + "1"
        elif current.parent != None:
            if code_list[current.char_ascii] == "":
                code_list[current.char_ascii] = curr_str
            if current.is_left():
                current = current.parent
                current.left = None
                curr_str = curr_str[:-1]
            elif current.is_right():
                current = current.parent
                current.right = None
                curr_str = curr_str[:-1]
        else:
            return code_list
       
def create_header(freq_list: list) -> str:
    '''Creates and returns a header for the output file'''
    header = ""
    for idx in range(len(freq_list)):
        if freq_list[idx] != 0:
            header += str(idx)
            header += " "
            header += str(freq_list[idx])
            header += " "
    return header[:-1]

def huffman_encode(in_file: str, out_file: str) -> None:
    '''Uses the Huffman code process on the input file and writes encoded text to output file'''
    input = open(in_file, "r", newline='')
    output = open(out_file, "w")
    freq_list = cnt_freq(in_file)
    huff_tree = create_huff_tree(freq_list)
    header = create_header(freq_list)
    huff_code = create_code(huff_tree)
    output.write(header)
    output.write("\n")
    for line in input:
        for char in line:
            code = huff_code[ord(char)]
            output.write(code)
    input.close()
    output.close()