
# Question 1.1: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Solution using bit vector (assuming only lowercase 'a' to 'z')
def isUnique_bitVector(string):
    checker = 0
    for c in string:
        val = ord(c) - ord('a')  # Create an integer value for each character in the string
        mask  = 1 << val
        if (checker & mask) > 0: # Perform bitwise AND. If the bit is already set, character is not unique
            return False
        checker |= mask          # Set the bit for this character
    return True
    

# Test cases  
print(isUnique_bitVector("abcdefg"))  # True
print(isUnique_bitVector("pizza"))  # False


# Algorithm runs in O(n) time and uses O(1) space.