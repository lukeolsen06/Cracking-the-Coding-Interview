

def isUnique_bitVector(s):
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        mask  = 1 << val
        if (checker & mask) > 0:
            return False
        checker |= mask
    return True
    
    
print(isUnique_bitVector("abcdefg"))  # True
print(isUnique_bitVector("pizza"))  # False