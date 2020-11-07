class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.head = self.Node((key, value))

    def add_to_head(self, key,value):
        node = Node((key, value))
        node.next = self.head
        self.head = node
            

    def delete(self,key):
        if self.head.value[0] == key:
            node = self.head.value
            self.head = self.head.next
            return node
        else:
            node = self.head
            while node.next is not None:
                if node.next.value[0] == key:
                    next_node = node.next.value
                    node.next = node.next.next
                    
                    return next_node
                node = node.next



    def find(self,key):
        node = self.head
        while node is not None:
            if node.value[0] == key:
                return node.value[1]
            node = node.next
        return None


    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next= None
        
        

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        #for load capacity per entry
        self.count = 0
        self.storage = [None for i in range(capacity)]

        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        #count
        return self.count/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        #     hash := FNV_offset_basis
        
        if not isinstance(key, bytes):
            key = key.encode('UTF-8', 'ignore')
        # for each byte_of_data to be hashed do
        hash = 14695981039346656037
        for x in key:
            hash ^= x
        #     hash := hash × FNV_prime
            hash *= 1099511628211
        #     hash := hash XOR byte_of_data
           

        return hash 


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        # Your code here
        # hashed_key = self.fnv1(key)
        # idx = hashed_key % self.capacity
        if self.get_load_factor() >= 0.70:
            self.resize(self.capacity*2)

        idx = self.hash_index(key)
      
        if self.storage[idx]!= None and self.storage[idx].find(key) is None:
            self.storage.add_to_head(key, value)
        elif self.storage[idx] is not None:
            node = self.storage[idx].head
            while node is not None:
                if node.value[0] == key:
                    node.value = (key,value)
                node = node.next
        else:
            self.storage[idx] = HashTableEntry(key, value)
        self.count+=1

        # new_node.next = self.head
        # self.head = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        """
        idx = self.hash_index(key)
        if self.storage[idx] == None:
            print("warning nothing to delete")
            return None
        else:
            # self.storage[idx].value = None
            # self.count-=1
            node = self.storage[idx].delete(key)
            if node is None:
                print("node not found")
            else:
                self.count -= 1
            if self.storage[idx].head == None:
                self.storage[idx] = None


        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity//2)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        if self.storage[idx] is not None:
            return self.storage[idx].find(key)
        else:
            return None
       
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        x = []

        for i in self.storage:
            if i is not None:
                node = i.head
                while node is not None:
                    x.append(node.value)
                    node = node.next
        self.capacity = new_capacity
        self.storage = [None for i in range(self.capacity)]
        for i in x:
            self.put(i[0], i[1])



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
