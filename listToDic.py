# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
def hashing_func(key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    # for inserting into hash table
    # hash_table[hash_key] =value
    # collision handling using chaining
    hash_table[hash_key].append((key, value))


def search(hash_table, key):
    hash_key = hashing_func(key)
    for c, val in enumerate(hash_table[hash_key]):
        k, v = val
        if key == k:
            print("key found with value: ", v)
            return 1
        print("key not found")
        return 0


# delete the key, value pair from hash table
def delete(hash_table, key):
    hash_key = hashing_func(key)
    key_exists = 0
    key_exists = search(hash_table, key)
    if key_exists == 1:
        hash_table[hash_key] = None
        print('Key {} deleted'.format(key))
    else:
        print('Key {} not found'.format(key))


# increment the key in the case of linear probing -> collision
def increment(hash_table, key):
    return (key + 1) % len(hash_table)


# displays a list as None
# hash_table = [None]*10

# for collision using chaining (linked list)
hash_table = [[] for i in range(11)]
# for collision using linear probing

print(len(hash_table))
# to perform insert to hash table with duplicate indexes
n = int(input("length of the list:\n"))
for i in range(0, n):
    key = int(input("enter the key:\n"))
    value = input("enter the value:\n")
    insert(hash_table, key, value)
print(hash_table)
# search for the key in hash table
print("enter the key to search: \n")
key_search = int(input())
print(search(hash_table, key_search))

# delete the key, value pair from hash table
print("enter the key to delete: \n")
key_delete = int(input())
delete(hash_table, key_delete)
print(hash_table)
