# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


# Python program to illustrate string
# with unique characters using
# brute force technique - O(n^2)

def uniqueCharacters(string):
    # If at any time we encounter 2
    # same characters, return false
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

            # If no duplicate characters encountered, return true
    return True


# Driver Code
str = input("enter the string:\n").lower()

if uniqueCharacters(str):
    print("The String ", str, " has all unique characters");
else:
    print("The String ", str, " has duplicate characters");


