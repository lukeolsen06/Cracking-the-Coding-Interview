
# Question 1.3 - URLify
# Write a method to replace all spaces in a string with a '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string

# BF: Iterate through the entire string and replace each space with '%20'. Runs in O(length) time because it checks every character up until the true length of the string

# Optimized: Determine the difference between input string length (with the trailing spaces) and the true string length. Then, divide the difference by 2 because we have two extra characters in '%20' for each space character ' '
# This will also be O(n) time but adds condition to see if we already have seen all the spaces in the true string. Drastically improves run time on extreme cases where there a few spaces in the beginning and a long run of no spaces at the backend of the string.

# Key assumption for this implementation: Trailing spaces are not counted in the true length of the string. Important question to ask
def URLify(string, length):
    if (length == 0):
        return 0
    num_spaces = (len(string) - length) // 2    # len(string) is the total length of the input string including the buffer. 
    chars = list(string)                       # convert string into a list of chars because strings in python are immutable
    for i, c in enumerate(chars):
        if c == ' ':
            chars[i] = '%20'
            num_spaces -= 1
            if (num_spaces == 0):
                return ''.join(chars)



# Book solution (pg 195). This is the traditional in-place solution that works backwards and modifies the string (list) in place. O(n) runtime, O(n) space
# Avoids assumption of trailing spaces not being counted in the true length of the string.
def URLify_2(string, length):
    """URLify working backwards from the end - the classic in-place solution."""
    chars = list(string)
    
    # Count spaces in the true string
    num_spaces = 0
    for i in range(length):
        if chars[i] == ' ':
            num_spaces += 1
    
    # Calculate the end index after URLification
    # Each space becomes 3 chars instead of 1, so +2 per space
    write_index = length + num_spaces * 2
    
    # Work backwards from the end of the true string
    for read_index in range(length - 1, -1, -1):
        if chars[read_index] == ' ':
            # Replace space with %20 (backwards)
            chars[write_index - 1] = '0'
            chars[write_index - 2] = '2'
            chars[write_index - 3] = '%'
            write_index -= 3
        else:
            # Copy the character
            chars[write_index - 1] = chars[read_index]
            write_index -= 1
    
    return ''.join(chars[:length + num_spaces * 2])


#Test cases
print(URLify("Doctor J  ", 8))        # Doctor%20J
print(URLify("Mr John Smith    ", 13))  # Mr%20John%20Smith
print(URLify(" Basketball  ", 11))       # %20Basketball
print(URLify(" John  ", 5))              # %20John     