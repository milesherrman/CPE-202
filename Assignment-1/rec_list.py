# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

def first_string(strlist: list) -> str:
    '''Recursively finds and returns "first" string in a given string list'''
    if strlist == None:
        return None
    elif strlist.rest == None:
        return strlist.value
    else: 
        curr_str = strlist.value
        next = first_string(strlist.rest)
        if next != None and next < curr_str:
            return next
        return curr_str

def split_list(strlist: list):
    '''Return a tuple with 3 lists (nodes) based on first character'''
    vowels = "aeiouAEIOU"
    if strlist == None:
        return None
    else: 
        val = strlist.value
        print(val)
        rec = split_list(strlist.rest)
        if rec == None:
            rec = (None, None, None)
        if val[0] in vowels:
            return Node(val, rec[0]), rec[1], rec[2]
        elif val[0].isalpha() == True:
            return rec[0], Node(val, rec[1]), rec[2]
        else: 
            return rec[0], rec[1], Node(val, rec[2])
        
temp = ["Yellow", ["abc", ["$7.25"]]]
temp = ["Yellow", "abc", "$7.25", "lime", "42", "Ethan"]
print(repr(temp))
print(temp)
mylist = Node("dog", [])
mylist = Node("cat" , mylist)
mylist = Node("fish", mylist)
print(mylist)
print(repr(mylist))
print(str(mylist))