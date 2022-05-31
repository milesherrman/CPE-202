from types import new_class


class HashTable:

    def __init__(self, table_size = 191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table
        self.list_of_keys = []
        
    def insert(self, key, value):
        """ Inserts an entry into the hash table """
        
        if self.in_table(key):
            #if in the table get index and assign value
            index = self.get_index(key)
            self.hash_table[index][1] = value
        else:
            #if it's not in the table, insert it by generating an index
            index = self.horner_hash(key) % self.table_size
            i = 1
            quadIndex = index
            while self.hash_table[quadIndex]:
                #while there is something at the location you are trying to insert, quad prob until there is nothing
                quadIndex = index + i**2
                quadIndex = quadIndex % self.get_table_size()
                i +=1
            #insert element and quad probed position
            self.hash_table[quadIndex] = [key, value]
            self.num_items += 1
            
        if self.get_load_factor() > 0.5:
            keys = self.get_all_keys()
            tempHash = HashTable(self.table_size * 2 + 1)
            for key in keys:
                value = self.get_value(key)
                tempHash.insert(key, value)
            self.hash_table = tempHash.hash_table
            self.table_size = self.table_size*2 + 1
                
    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        n = min(len(key), 8) - 1
        i = 0
        hash = 0
        while i <= n:
            hash += ord(key[i]) * 31 ** (n - i)
            i += 1
        return hash%self.table_size
            
    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        index = self.get_index(key)
        return True if index else False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        hash = self.horner_hash(key)
        if self.hash_table[hash]:
            if self.hash_table[hash][0] == key:
                return hash
            else:
                n = 1
                quadIdx = hash
                while self.hash_table[quadIdx] and self.hash_table[quadIdx][0] != key:
                    quadIdx = hash + n**2
                    quadIdx = quadIdx % self.get_table_size()
                    n = n + 1
                if self.hash_table[quadIdx] == None:
                    return None
                else: 
                    return quadIdx   
        else:
            return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        keys = []
        for entry in self.hash_table:
            if entry != None:
                keys.append(entry[0])
        return keys

    def get_value(self, key):
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        idx = self.get_index(key)
        if idx == None:
            return None
        return self.hash_table[idx][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

