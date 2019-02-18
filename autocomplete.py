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
    def __init__(self, value=None, i=None):
        self.value = value
        self.dict = {}
        self.end = False
        self.count = 0 # how many words contain this prefix
        self.depth = i # how many letters into the word, 0 = first letter


def buildTrie(array):
    root = Trie()
    current = root
    for word in array:
        # print("word " + word + '\n')
        for i, char in enumerate(word):
            c = char.lower()
            if c not in current.dict:
                # print('adding!')
                current.dict[c] = Trie(c,i)
            current.count += 1
            current = current.dict[c]
            # print('char ' + current.value)
        current.end = True
        # print(count, current.value, current.end)
        current = root
    # print(root.count)
    return root
#this works (tested)


array = dict()
root = buildTrie(array)
# print(root)

# current = root
# count = 0
# while current:
#     count+=1
#     print(current.depth, count, current.count)
#     current = current.dict['a']


# current = root.dict['a'].dict['u']
# print(current.dict)
# for key in root.dict:
#     print(key)

def findWords(pre, root):
    # alpha = list('abcdefghijklmnopqrstuvwxyz')
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

    for char in pre: #move up to the correct point in the dictionary
        if char in current.dict:
            current = current.dict[char]
            print(char)
        # else:
        #     return 'no words exist in English that start like that'

    known = current #the correct point in the tree based on the prefix
    suffixCount = known.count
    # print(suffixCount)

    # while suffixCount > 0:

    def goIn(node):
        # depthChars = node.dict.keys()
        for key in node.dict:
            print(node.dict[key].value,node.dict[key].depth)
            # w.append(node.dict[key].value)
            # if node.dict[key].end == True:
            #     break
            goIn(node.dict[key])
            # return node.dict[key].value

    words.append(goIn(known))



    #

    # for _ in range(len(alpha)):
    #     # print(alpha[_],current.dict)
    #     if alpha[_] in current.dict:
    #         current = current.dict[alpha[_]]
    #         word += current.value
    #     else:
    #         if current.end == True and word not in words:
    #             words.append(word)
    #         word = pre

    #
    # while current.dict[_].end == False:
    #     if
    # words.append(rec(word, known))
    return words


print(findWords('aard', root))
