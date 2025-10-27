
# Question 1_2: Given two strings, write a method to decide if one is a permutation of the other.

# Ex. "John" -> "nhoJ"

# BF: Sort both strings and compare: O (n log n)

# Implementation using hash table. O(n) runtime, O(k) space complexity for each unique character having to be stored in table, up to O(n) if all are distinct
def is_permutation_1(s1, s2):
    if (len(s1) != len(s2)):
        return False
    freq = {}
    for c in s1:
        if c in freq:
            freq[c] += 1
        else: 
            freq[c] = 1
    seen = {}
    for c in s2:
        if c not in freq:
            return False
        else:
            if c in seen:
                if seen[c] == freq[c]:
                    return False
                else:
                    seen[c] += 1
            else:
                seen[c] = 1
    return True


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



print(is_permutation_1("Luke", "kuLe")) # True
print(permutation("Basketball", "basketball")) # False
print(permutation(" ", "")) # False



    

