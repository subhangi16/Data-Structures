# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# uses integer value called checker with respect to ASCII char set - Additional DS
# complexity is O(n)


def isunique1(string):
    if len(string) > 256:
        return False
    unique_tracker = 0
    for char in string:
        ascii_val = ord(char)
        if (unique_tracker & (1 << ascii_val)) > 0:
            return False
        unique_tracker |= (1 << ascii_val)
    return True


s = input("enter the string:\n").lower()
print(isunique1(s))
