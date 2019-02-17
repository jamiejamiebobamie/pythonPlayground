'''Trying to write an autocomplete function using a Trie. It's not working out.'''

import random

def dict():
    """opens the dictionary-words file at the path and assigns the file to f
    reads f and splits each word into an array element of the words array
    closes the file f
    and returns the array of dictionary words
    """
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words



class Trie:
    def __init__(self, value=None):
        self.value = value
        self.dict = {}
        self.end = False
        self.count = 0


def buildTrie(array):
    root = Trie()
    current = root
    for word in array:
        for i, char in enumerate(word):
            c = char.lower()
            if c not in current.dict:
                current.dict[c] = Trie(c)
                root.count += 1
            current = current.dict[c]
        current.end = True
        current = root
    return root



array = dict()
print('jom' in array)
root = buildTrie(array)

# current = root.dict['a'].dict['u']
# print(current.dict)
# for key in root.dict:
#     print(key)

def findWords(pre, root):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    # print(alpha)
    # def rec(pre, node):
    #     word = pre
    #     # alpha = ['abcdefghijklmnopqrstuvwxyz']
    #     count = len(alpha)
    #     current = node
    #     for _ in range(count):
    #         if _ in current.dict:
    #             word += _
    #             current = current.dict[alpha[_]]
    #         else:
    #             return word

    word = pre
    words = []
    current = root
    for char in pre:
        if char in current.dict:
            current = current.dict[char]
        else:
            return 'no words exist in English that start like that'

    known = current
    for _ in range(len(alpha)):
        # print(alpha[_],current.dict)
        if alpha[_] in current.dict:
            current = current.dict[alpha[_]]
            word += current.value
        else:
            if current.end == True and word not in words:
                words.append(word)
            word = pre

    #
    # while current.dict[_].end == False:
    #     if
    # words.append(rec(word, known))
    return words


print(findWords('poo',root))
