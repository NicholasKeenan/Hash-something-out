#A simple implementation of a hash table in python

#Node class to hold the key-value pairs for the hash table
class Node:
    def __init__ ( self, key, value ):
        self.key = key
        self.value = value
        self.next = None

###Hash Table 1###
#This implementation will use a movie class as the backbone
#where the title of the movie will be the key to store and retrieve the records
#this will be a linked list implementation

class HashTable1:
    def __init__ ( self, size, hash_func ):
        self.size = size
        self.table = [ None ] * size #initialize the hash table with None values
        self.hash_func = hash_func #assign the hash function to a variable for easy access
        self.collisions = 0 #initialize a counter for collisions

    def insert ( self, key, value ):
        index = self.hash_func ( key ) % self.size #calculate the index using the hash function and modulo operator
        new_node = Node ( key, value ) #create a new node with the key-value pair

        if self.table [ index ] is None: #if the index is empty, insert the new node
            self.table [ index ] = new_node
        else: #if there is a collision, add the new node to the end of the linked list
            current = self.table [ index ]
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.collisions += 1 #increment the collision counter

    def lookup ( self, key ):
        index = self.hash_func ( key ) % self.size #calculate the index using the hash function and modulo operator
        current = self.table [ index ] #get the node at the calculated index

        while current is not None: #traverse the linked list at the index to find the key
            if current.key == key: #if the key is found return the value
                return current.value
            current = current.next #move to the next node in the linked list
        
        return None #if the key is not found, return None

    def find_wasted_space ( self ):
        return sum ( 1 for bucket in self.table if bucket is None ) #count the number of empty buckets in the hash table
    
###Hash Table 2###
#This implementation will use a movie class as the backbone
#where the quote of the movie will be the key to store and retrieve the records
#this will be a linear probing implementation, where in case of a collision, the next available bucket will be used

class HashTable2:
    def __init__ ( self, size, hash_func ):
        self.size = size
        self.table = [ None ] * size #initialize the hash table with None values
        self.hash_func = hash_func #assign the hash function to a variable for easy access
        self.collisions = 0 #initialize a counter for collisions

    def insert ( self, key, value ):
        index = self.hash_func ( key ) % self.size #calculate the index using the hash function and modulo operator

        while self.table [ index ] is not None: #if there is a collision, increment the index until an empty bucket is found
            index = ( index + 1 ) % self.size #increment the index and wrap around if it exceeds the size of the table
            self.collisions += 1 #increment the collision counter
        
        self.table [ index ] = Node ( key, value ) #insert the new node at the calculated index

    def lookup ( self, key ):
        index = self.hash_func ( key ) % self.size #calculate the index using the hash function and modulo operator
        startIndex = index #store the starting index to detect if we have looped through the entire table
        while self.table [ index ] is not None: #traverse the table to find the key
            storedKey, storedValue = self.table [ index ]
            if storedKey == key: #if the key is found return the value
                return storedValue
            index = ( index + 1 ) % self.size #increment the index and wrap around if it exceeds the size of the table
            if index == startIndex: #if we have looped through the entire table and come back to the starting index, the key is not found
                break
        
        return None #if the key is not found, return None

    def find_wasted_space ( self ):
        return sum ( 1 for bucket in self.table if bucket is None ) #count the number of empty buckets in the hash table