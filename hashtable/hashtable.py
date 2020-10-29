class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

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
        self.head = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        #     hash := FNV_offset_basis
        key = 14695981039346656037

        # for each byte_of_data to be hashed do
        for x in key:
        #     hash := hash × FNV_prime
            x = x * 1099511628211
        #     hash := hash XOR byte_of_data
            x = x ^ key

        return x 


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
        hashed_key = self.fnv1(key)
        idx = hashed_key % self.capacity
        new_node = HashTableEntry(idx, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
         # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store head node 
        temp = self.head 
  
        # If head needs to be removed
        hashed_key = self.fnv1(key)
        idx = hashed_key % self.capacity
        if idx == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(idx -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        hashed_key = self.fnv1(key)
        idx = hashed_key % self.capacity
        current = self.head  # Initialise temp 
        count = 0  # Index of current node 
  
        # Loop while end of linked list is not reached 
        while (current): 
            if (count == idx): 
                return current.value 
            count += 1
            current = current.next
  
        # if we get to this line, the caller was asking 
        # for a non-existent element so we assert fail 
        assert(false) 
        return None
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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
