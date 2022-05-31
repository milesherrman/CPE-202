
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] 
        self.num_items = 0
        self.num_collisions = 0
    
    def __repr__(self):
        return "Hash: " + str(self.hash_table)

    def insert(self, key: int, value: any) -> None:
        """Insert the key-item pair into the hash table"""
        try:
            valid_key = int(key)
            if valid_key < 0:
                raise ValueError
            elif key % 1 != 0:
                raise ValueError
        except:
            raise ValueError
        
        hash_value = key % self.table_size
        new = (key,value)
        if self.hash_table[hash_value] == []:
            self.hash_table[hash_value].append(new)
            self.num_items = self.num_items + 1
        else:
            duplicate = False
            for idx in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][idx][0] == key:
                    self.hash_table[hash_value][idx] = new
                    duplicate = True
            if duplicate == False:
                self.num_items = self.num_items + 1
                if self.load_factor() > 1.5:
                    self.num_items = 0
                    self.num_collisions = 0
                    hash = self.hash_table
                    self.hash_table = [[] for _ in range(self.table_size*2 + 1)]
                    self.table_size = self.table_size*2 + 1
                    for sublist in hash:
                        for item in sublist:
                            self.insert(item[0], item[1])
                    self.insert(key, value)
                else:
                    self.num_collisions = self.num_collisions + 1
                    self.hash_table[hash_value].append(new)    
    
    def get_item(self, key: int) -> any:
        """Returns the item from the hash table associated with the key."""
        hash_value = key % self.table_size
        for pair in self.hash_table[hash_value]:
            if pair[0] == key:
                return pair[1]
        raise LookupError

    def remove(self, key: int) -> tuple:
        """Removes and returns key-item pair from the hash table"""
        try:
            hash_value = key % self.table_size
            for pair in self.hash_table[hash_value]:
                if pair[0] == key:
                    self.hash_table[hash_value].remove(pair)
                    self.num_items = self.num_items - 1
                    return pair
        except:
            raise LookupError

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions