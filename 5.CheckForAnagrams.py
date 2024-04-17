# Check whether two given strings X and Y of sizes N and M respectively are anagram of each other or not.

# Sample Input
# input: N = 4, X = abcd, M = 4, Y = dacb
# Sample Output
# Output: Yes
# Sample Explanation
# All the characters of string "abcd" is present in "dacb" and in same frequencies. Hence both are anagram of each other.

# Expected Time Complexity
# O(NLog(N)), where N is the lenght of the given string

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N,M <= 100000

# Time Complexity:
# Building the frequency dictionaries for strings X and Y:
# This step iterates through each character in the strings X and Y once, resulting in a time complexity of O(N + M), where N is the length of string X and M is the length of string Y.
# Comparing the frequencies of characters in the two dictionaries:
# This step iterates through each key in the dictionary dictX, resulting in a time complexity of O(N) in the worst case.
# Overall, the time complexity of the code is O(N + M), where N is the length of string X and M is the length of string Y.

# Space Complexity:
# Storing the frequencies of characters in dictionaries dictX and dictY:
# In the worst case, all characters of the string X (or Y) are unique, resulting in a space complexity of O(N) for dictX and O(M) for dictY.
# Thus, the space complexity of the code is O(N + M).
# In summary, the time complexity of the code is O(N + M), and the space complexity is O(N + M), where N is the length of string X and M is the length of string
def f():
    N = 4
    X = 'abcd'
    M = 4
    Y = 'dacb'
    if N!=M:
        return False
    dictX={}
    for i in range(N):
        if X[i] not in dictX:
            dictX[X[i]]=1
        else:
            dictX[X[i]]+=1
    
    dictY={}
    for i in range(M):
        if Y[i] not in dictY:
            dictY[Y[i]]=1
        else:
            dictY[Y[i]]+=1
    
    for i in dictX:
        if i not in dictY:
            return False
        elif dictX[i]!=dictY[i]:
            return False
    return True
print(f())

#Better 
# Time Complexity: O(n log n) - Sorting the strings takes O(n log n) time.
# Space Complexity: O(n) - Space required to store the sorted strings.

def anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


#2nd- Approach