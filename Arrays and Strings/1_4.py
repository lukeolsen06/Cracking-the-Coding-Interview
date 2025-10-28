# Question 1.4: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# Example: "Tact Coa" -> True (permutations: "taco cat", "atco cta", etc.)

# Assumptions: ASCII characters only, case insensitive, spaces are ignored, special characters can be used but there must be at least one letter in the string.

# BF: Walk through the string and count the frequency of each character. If more than one character has an odd frequency, it is not a palindrome.

# O(n) runtime, O(n) space using hash table
def is_perm_palindrome(string):
    s = string.lower()
    assert any(c.isalpha() for c in s)
    freq = {}
    for c in s:
        if c != ' ':
            freq[c] = freq.get(c, 0) + 1
    count = 0
    for el in freq:
        if (freq[el] % 2 == 0):
            continue
        else:
            count += 1
            if count > 1:
                return False
    return True


print(is_perm_palindrome("Taccct Coa")) # True
print(is_perm_palindrome("Basketball Team")) # False
print(is_perm_palindrome("duvkfldlvuk f")) # True





# Optimize: Use a bit vector for O(1) space
def is_perm_palindrome_2(string):
    s = string.lower()
    assert any(c.isalpha() for c in s)

    bit_vector = 0
    for c in s:
        if c != ' ':
            bit_vector ^= (1 << (ord(c) - ord('a')))
    
    return bit_vector == 0 or(bit_vector & (bit_vector - 1)) == 0


print("\n")
print(is_perm_palindrome_2("Taccct Coa")) # True
print(is_perm_palindrome_2("Basketball Team")) # False
print(is_perm_palindrome_2("duvkfldlvuk f")) # True
print(is_perm_palindrome_2("   $%^  ")) # Assertion error
    
