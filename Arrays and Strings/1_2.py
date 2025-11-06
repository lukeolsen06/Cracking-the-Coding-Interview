
# Question 1.2: Given two strings, write a method to decide if one is a permutation of the other.

# Ex. "John" -> "nhoJ"

# BF: Sort both strings and compare: O (n log n)

# Implementation using hash table. O(n) runtime, O(k) space complexity for each unique character having to be stored in table, up to O(n) if all are distinct
def is_permutation_1(s1, s2):
    if (len(s1) != len(s2)): # If strings are not the same length, they cannot be permutations of each other
        return False
    freq = {}                # Frequency table to store the number of times each character appears in s1
    for c in s1:
        if c in freq:
            freq[c] += 1     # If character is already in table, increment count
        else: 
            freq[c] = 1      # If character is not in table, add it with count 1
    seen = {}                # Frequency table to store the number of times each character appears in s2
    for c in s2:
        if c not in freq:
            return False     # If character is not in s1, it cannot be a permutation of s1
        else:
            if c in seen:
                if seen[c] == freq[c]:
                    return False       # If character appears more times in s2 than s1, it cannot be a permutation of s1
                else:
                    seen[c] += 1
            else:
                seen[c] = 1
    return True                        # If we get through all characters without returning False, they are permutations of each other


# Book solution (pg 194). O(n) runtime, O(128) -> O(1) space complexity assuming ASCII characters
def permutation(s1, s2):
    if (len(s1) != len(s2)):
        return False
    letters = [0] * 128
    for c in s1:
        letters[ord(c)] += 1
    for c in s2:
        letters[ord(c)] -= 1
        if (letters[ord(c)]) < 0:
            return False
    return True


# Test cases
print(is_permutation_1("Luke", "kuLe")) # True
print(permutation("Basketball", "basketball")) # False
print(permutation(" ", "")) # False


# Most optimal solution: O(n) runtime and O(1) space

    

