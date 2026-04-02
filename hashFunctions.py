#functions for hashing and collision resolution

def linkedList_poor ( key ):
    return len ( key ) #this hash function will return the length of the key, which is not a good hash function because it will cause collisions for keys of the same length

def linkedList_good ( key ):
    total = 0
    for char in key:
        total += ord(char)
    return total #this hash function will return the sum of the ASCII values of the characters in the key

def linearProbing_poor ( key ):
    return len ( key ) #this hash function will return the length of the key, which is not a good hash function because it will cause collisions for keys of the same length

def linearProbing_good ( key ):
    total = 0
    for char in key:
        total += ord(char)
    return total #this hash function will return the sum of the ASCII values of the characters in the key