# There is a new alien language which uses the latin alphabet.
# However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary,
# where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example 1:
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
#
# Example 2:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
#
# Example 3:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".
#
# Note:
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

array = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

class Trie:
    def __init__(self, value=None):
        self.value = value
        self.dict = {}
        self.end = False

root = Trie()

def buildTrie(array):
    current = root
    for word in array:
        for i, char in enumerate(word):
            if char not in current.dict:
                current.dict[char] = Trie(char)
                # print(char, current.dict)
            print(char, i, len(word)-1,current.value, current.dict)
            current = current.dict[char]
        current.end = True
        current = root



# def traverseTrie(root):
#     def __helper(branch):
#         arr = []
#         current = root
#         while current:
#             arr.append(current.dict)
#             print(arr)
#             current = current.dict[arr]
#         return arr
#     return __helper(root)

buildTrie(array)
