#functions for hashing and collision resolution

def linkedList_poor ( key ):
    return len ( key ) #this hash function will return the length of the key, which is not a good hash function because it will cause collisions for keys of the same length

def linkedList_good ( key ):
    total = 0
    for char in key:
        total += ord(char)
    return total #this hash function will return the sum of the ASCII values of the characters in the key

def linkedList_better ( key ):
    total = 0
    for char in key:
        total += ord(char) * (key.index(char) + 1) #multiply the ASCII value of the character by its index so it is less likely to collide
    return total

def linkedList_better2 ( key ):
    total = 0
    for char in key:
        total += ord(char) * (key.index(char) + 1) #multiply the ASCII value of the character by its index so it is less likely to collide
    return total * len ( key ) #multiply the total by the length of the key to reduce collisions again

def linkedList_best ( key ):
    total = 0
    for char in key:
        total += ord(char) * (key.index(char) + 1) #multiply the ASCII value of the character by its index so it is less likely to collide
    return total * len ( key ) * 509 #multiply the total by the length of the key and a large prime number to reduce collisions

def linearProbing_poor ( key ):
    return len ( key ) #this hash function will return the length of the key, which is not a good hash function because it will cause collisions for keys of the same length

def linearProbing_good ( key ):
    total = 0
    for char in key:
        total += ord(char)
    return total #this hash function will return the sum of the ASCII values of the characters in the key

def linearProbing_better ( key ):
    total = 0
    for char in key:
        total += ord(char) * (key.index(char) + 1) #multiply the ASCII value of the character by its index so it is less likely to collide
    return total