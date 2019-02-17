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

# *******************
# array = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# class Trie:
#     def __init__(self, value=None):
#         self.value = value
#         self.dict = {}
#         self.end = False
#
# root = Trie()
#
# def buildTrie(array):
#     current = root
#     for word in array:
#         for i, char in enumerate(word):
#             if char not in current.dict:
#                 current.dict[char] = Trie(char)
#                 # print(char, current.dict)
#             print(char, i, len(word)-1,current.value, current.dict)
#             current = current.dict[char]
#         current.end = True
#         current = root
#
# buildTrie(array)

# I built a trie data structure, but it appears this problem does not require that...

# *******************

# array = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# iterate through the words in the array,
# put the first letter of each word into a new array
# then put all of the second letters into the new array
# iterate through the words, putting their letters into the new array
# in the order they occur in the list (first)
# and in the words (second).
# once all letters from the words have been put into the new array in ascending order
# iterate through the new array. the first occurence of the letter is its order in the alien alphabet
# all later occurences of the letter should be removed from the new array
# return new array with single instances of the letters.


# def letterOrder(array):
    # arr = []
    # i = 0
    # j = 0
    # while i < len(array):
    #     while j < i:
    #         if i
    #         arr.append(array[i][j])
    #         i += 1
    #         break
    #
    # print(arr)
#     arr = []
#     i = 0
#     while len(array) > 0:
#         while i < len(array[i]):
#             array[i] = list(array[i])
#             print(array[i])
#             arr.append(array[i].pop(0))
#             i += 1
#         else:
#             i = 0
#     print(arr)
#
#
# array = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# array = ["z","x","z"]

array = [
  "z",
  "x"
]

array = ['a',
"abandon",
"abandoned",
"ability",
"able",
"about",
"above",
"abroad",
"absence",
"absent",
"absolute",
"absolutely",
"absorb",
"abuse",
"abuse",
"academic",
"accent",
"accept",
"acceptable",
"access",
"accident",
"accidental",
"accidentally",
"accommodation",
"accompany",
"according",
"account",
"account",
"accurate",
"accurately",
"accuse",
"achieve",
"achievement"
]

def letterOrder(array):
    A = []
    i = 0
    wordCount = len(max(array))
    stored = array[0][0]
    print(stored)
    while wordCount > 0:
        for j, word in enumerate(array):
            seen = []
            if i < len(word):
                if word[i] not in A:
                    A.append(word[i])
        i += 1
        wordCount -=1
    return A


print(letterOrder(array))


                    #   Letters can occur twice,
                    #   but they cannot occur
                    #   twice in the same index of different words
                    #   after not occuring once.

                    #   Example 'n' in the second index:
                    #   another
                    #   ant
                    #   ape
                #X  #   antelope <---incorrect

                    #   need to push to an array that gets cleared
                    #   after a change in index
                    #   that stores letters
                    #   that have come before
                    #   and have been followed by a new letter

                    #   Example above:
                    #   'n' would get pushed to the array once 'p' in 'ape'
                    #   was operated on.
