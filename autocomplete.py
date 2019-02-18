'''Wrote an autocomplete function. Type a word wrapped in strings into the
first arugment of the findWord() function at the bottom to generate all possibilites.

TO-DO: Organize code into classes within classes and methods within classes.'''



import random

def dict():
    """opens the dictionary-words file at the path and assigns the file to 'f'
    reads 'f' and splits each word into an array element of the 'words' array
    closes the file 'f'
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

    for char in pre: #move up to the correct point in the dictionary
        if char in current.dict:
            current = current.dict[char]
            # print(char)
        # else:
        #     return 'no words exist in English that start like that'

    known = current #the correct point in the tree based on the prefix
    suffixCount = known.count
    print(suffixCount)

    # while suffixCount > 0:

    def goIn(node, w, sC):
        co = sC #passing off the suffix count to the interior scope
        # depthChars = node.dict.keys()
        for key in node.dict:
            c = w
            # print(node.dict[key].value,node.dict[key].depth)
            c += node.dict[key].value
            # print(node.dict[key].count)
            # print(c)
            if node.dict[key].end == True:
                words.append(c)
                if co < 0: # if the suffix you enter is a complete word (like 'ant')...
                    return c
                else:
                    co -= 1
                # print(c, True, words)
                # w = ''
            goIn(node.dict[key], c, co)
            # return node.dict[key].value

    # words.append(goIn(known, pre))
    goIn(known, pre, suffixCount)



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

print(findWords('ant', root)) #type in prefix

# alpha = list('abcdefghijklmnopqrstuvwxyz')
#
# current = root
# alphabetTest = []
# for _ in range(len(alpha)):
#     max = [None,0]
#     for key in current.dict:
#         if max[1] < current.dict[key].count:
#             max[0] = current.dict[key].value
#             max[1] = current.dict[key].count
#     alphabetTest.append(max)
#     if alpha[_] in current.dict:
#         current = current.dict[alpha[_]]
#
# print(alphabetTest)
