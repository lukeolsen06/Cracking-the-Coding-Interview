# Question 1.9: String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
# (e.g., "waterbottle" is a rotation of "erbottlewat").

# Runtime: O(n) where n is the length of the strings
# Space: O(n) where n is the length of the strings

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)

# Example implementation of isSubstring
def isSubstring(s1, s2):
    return s2 in s1

print(string_rotation("waterbottle", "erbottlewat")) # True
print(string_rotation("evermore", "ermoreev"))       # True
