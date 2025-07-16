## Description:A chained hashtable is a data structure with stored key-values that can efficiently accomplish a collision by linking duplicates with pointers. Operation of inserting, searching, deleting, and resizing are controlled according to the present load factor.
    
class HashTableChaining:
    def __init__(self, size=10):
        # Setting the initial size of the table
        self.size = size
        
        # Creating an empty list for each slot
        self.table = [[] for _ in range(size)]
        
        # Starting the element count at zero
        self.count = 0

    def hash_function(self, key):
        # Calculating the index using built-in hash and table size
        return hash(key) % self.size

    def insert(self, key, value):
        # Finding the correct index for the key
        index = self.hash_function(key)
        
        # Checking if the key already exists and updating value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        # Adding the new key-value pair to the chain
        self.table[index].append([key, value])
        
        # Increasing the count of elements
        self.count += 1

        # Resizing the table if the load factor is too high
        if self.load_factor() > 0.75:
            self.resize()

    def search(self, key):
        # Finding the index for the key
        index = self.hash_function(key)
        
        # Looking through the chain to find the key
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        
        # Returning None if the key is not found
        return None

    def delete(self, key):
        # Finding the index for the key
        index = self.hash_function(key)
        
        # Searching for the key and removing it
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                
                # Reducing the count of elements
                self.count -= 1
                return True
        
        # Returning False if the key is not found
        return False

    def load_factor(self):
        # Calculating the ratio of elements to table size
        return self.count / self.size

    def resize(self):
        # Saving the old table before resizing
        old_table = self.table
        
        # Doubling the table size
        self.size *= 2
        
        # Resetting the count and creating a new table
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        
        # Reinserting all elements from the old table
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

# Running example operations on the hash table
if __name__ == "__main__":
    # Creating a new hash table
    ht = HashTableChaining()
    
    # Inserting some key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grape", 30)

    # Searching for a key and printing the result
    print("Search banana:", ht.search("banana"))
    
    # Deleting a key and printing the result
    print("Delete grape:", ht.delete("grape"))
    
    # Searching again for a deleted key
    print("Search grape:", ht.search("grape"))
    
    # Printing the current load factor
    print("Current load factor:", ht.load_factor())
