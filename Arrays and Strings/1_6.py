# Question 1.6: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

# BF: Iterate through the string and count the number of consecutive characters. Add the index character and its count to a new string copy. This would result in O(n^2) time complexity, which is not ideal.

# Optimized: Use a list to store the compressed string. This would result in O(n) time complexity and O(n) space complexity.
def compress(s):
    newString = [] # List to store the compressed string
    i = 0
    while (i < len(s)):
        count = 1
        while ((i < len(s) - 1) and s[i] == s[i+1]): # Count the number of consecutive characters
            count += 1
            i += 1
        newString.append(s[i]) # Add the character to the compressed string
        newString.append(str(count)) # Add the count to the compressed string
        i += 1
    compressed = ''.join(newString)
    return compressed if len(compressed) < len(s) else s


print(compress("aabcccccaaa")) # a2b1c5a3
print(compress("abcddddd")) # abcddddd
print(compress("abcdddddd")) # a1b1c1d6
print(compress("abcd")) # abcd
print(compress("ababababababababababababab")) # Should be this original string

