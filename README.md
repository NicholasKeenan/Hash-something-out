COS-226: Hash Something Out - Reflection

I implemented two types of hash tables to store fake movie records
  Linked list hash table
  Linear probing hash table

1. linkedList_poor
2. linkedList_good
3. linkedList_better
4. linkedList_better2
5. linkedList_best

6. linearProbing_poor
7. linearProbing_good
8. linearProbing_better
9. linearProbing_better2
10. linearProbing_best

For each of the two hash tables I created the same five hash functions. Function one took the length of the key as the hash. 
This caused it to have a large amount of collisions (3,298,665 for linked list and 112,214,903 for linear probing).
The second function takes the sum of the ASCII values of the characters in the key. This improved collisions and time
spent in lookup and construction time. In the case of linear probing it cut the construction and lookup times nearly in half.
Function three multiplied the ASCII value of the character by its index. Once again this was to try and improve the amount of collisions.
The result of this was the best of all. Linked list fell in collisions but increased its construction and lookup times. Linear probing saw 
saw its collisions drop from just short of a billion down to 9696 and their construction and lookup time dropped over 90%.
Function four did the same thing as three but then taking the product of the characters ASCII value and index, it then multiplies that by
the total length of the key. This did not increase the time to contruct or lookup but it did slightly increase collisions and wasted space for 
both hash tables. The fifth function once again taking the product of the characters ASCII value and index, but then multiplying it by 
the total length of the key as well as a large prime number. This had the exact same stats as number four.

Linked List Fastest Construction: Function 2
Linear Probing Fastest Construction: Function 3

Linked List Fastest lookup: Function 2
Linear Probing Fastest lookup: Function 3

Linked List Least Collisions: Function 3
Linear Probing Least Collisions: Function 3

Linked List Least Wasted Space: Function 3
Linear Probing Least Wasted Space: All had the same

Overall function three has the best stats in almost every category. The method of creating the most unqiue hashes 
was the most effective. The "randomness" provided by function three multiplying the ASCII values of the characters by its 
index allowed collisions to plummet which also heavily improved speed. After that, adding more randomness to it gave no 
benefit and became unnecessary complication.

