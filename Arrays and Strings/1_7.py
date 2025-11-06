# Question 1.7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?

# O(n^2) time, O(1) space

def rotate_matrix(m):
    n = len(m)
    for layer in range((n // 2)):
        first = layer
        last = n - 1 - layer
        i = first
        while (i < last):
            diff = i - first
            temp = m[i][first]
            m[i][first] = m[first][last-diff]
            m[first][last-diff] = m[last-diff][last]
            m[last-diff][last] = m[last][i]
            m[last][i] = temp
            i += 1
    return m

matrix = [[1,2,3,4],
          [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]
         ]

            # [[4,8,12,16],
            # [3,7,11,15],
            # [2,6,10,14],
            # [1,5,9,13]]

print(rotate_matrix(matrix))