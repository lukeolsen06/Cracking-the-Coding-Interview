# Question 1_5: One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# Ex: 
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# O(n) runtime, O(n) space.
# EDIT: The below implementation won't work for cases where the frequency counts are the same but the letters are jumbled. That's why it's important to check order (i.e., use a sliding window)
def one_away_ht(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    freq_1 = {}
    for c in s1:
        freq_1[c] = freq_1.get(c, 0) + 1
    
    freq_2 = {}
    for c in s2:
        freq_2[c] = freq_2.get(c, 0) + 1
    
    diffCount = 0
    for c in freq_1:
        if (diffCount > 1): return False
        if c not in freq_2: 
            diffCount += 1
            continue
        if (freq_1[c] == freq_2[c]):
            continue
        else:
            if (abs(freq_1[c] - freq_2[c]) == 1):
                diffCount += 1
            else:
                return False
    
    if (diffCount == 1 and len(s1) < len(s2)): # means that we have one or more character differences following character difference
        return False
    
    return True


# Sorting first doesn't make sense because that would be O(n log n)


# Sliding window implementation - O(n) time, were n is the length of the shorter string. O(1) space since we only use the diffCount variable, not two hash tables
def one_away_sw(s1, s2):
    differenceInLength = abs(len(s1) - len(s2))
    if abs(differenceInLength) > 1:
        return False
    
    if (len(s1) <= len(s2)):
        useString = s1
    else:
        useString = s2
    
    diffCount = 0
    for i, c in enumerate(useString):
        if c == s2[i]:
            continue
        else:
            diffCount += 1
        
    if ((diffCount > 1) or (diffCount == 1 and differenceInLength > 0)): # Since we are using the shorter string, if diffCount is 1 at the end, we know there is an extra character difference at the end
        return False
    else:
        return True


print(one_away_sw("pale", "ple")) # True
print(one_away_sw("pales", "pale")) # True
print(one_away_sw("bale", "pale")) # True
print(one_away_sw("pal", "pales")) # False
print(one_away_sw("John", "oh")) # False
print(one_away_sw("", "$")) # True
print(one_away_sw("bark", "karb")) # False

    

    
    

