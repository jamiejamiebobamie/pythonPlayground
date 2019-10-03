"""You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word
in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []"""

from collections import Counter

def cat(s,arr):
    result = []
    dict = {}
    histogram = Counter(arr) # reuce computation by looking for repeating words
    for word in arr:
        if word[0] not in dict:
            dict[word[0]] = [word]
        else:
            dict[word[0]].append(word)

    for i, char in enumerate(s[0]):
        if char in dict:
            print(char)
            for w in dict[char]:
                if s[0][i:len(w)] == 


    # you need to recursivley check to see if the characters match up with the words in the dict.


s = "barfoothefoobarman",
words = ["foo","foo","bar"]

cat(s,words)
