corpus = [["hey ho hey"], ["hey ho hey hey"], ["hey hey hey"]]


def bow(corpus):

    lookup = {}

    indexCount = 0


    for array in corpus:
        for line in array:
            string = line.split(" ")
            for word in string:
                if word not in lookup:
                    lookup[word] = indexCount
                    indexCount+=1
    result = [[0]* len(lookup)] * len(corpus)

    # print(lookup)
    # print(result)

    for i, array in enumerate(corpus):
        # print(result[i])
        for line in array:
            string = line.split(" ")
            for word in string:
                result[i][lookup[word]]+=1
                # print(word, i, lookup[word], result)
            # print(result)

    return result

# print(bow(corpus))
import collections

def retry(corpus):
    result = []
    arrays = []
    for line in corpus:
        # print(line)
        for word in line:
            arrays.append(word.split(" "))
    for array in arrays:
        result.append(collections.Counter(array))
    return result

# print(retry(corpus))


"""

Optimal approach:
Iterate through all of the words in the arrays in the corpus.

As you iterate through the words, pop them to a new array.
This array will serve as the dictionary, with the index in the array, the key.

As you pop the words from the corpus you replace them with a 1 or a zero.

The first array of words in the corpus will all be 1's with trailing zeroes
added to reperesent all of the words in the other arrays...

all of the arrays no matter their length will have the same length when they are returned
namely the length of all of the unique words in all of the arrays.

"""


import math

def retryRetry(corpus):
    lookup = {}
    for i, array in enumerate(corpus):
        for words in array:
            words = words.split(" ")
            # print(words)
            for word in words:
                if word not in lookup:
                    lookup[word] = len(lookup)
    print(lookup)

    result = [ [0]*len(lookup) ] * len(corpus)
                #2                   #3
    print(result)

    for i, array in enumerate(corpus):
        for words in array:
            words = words.split(" ")
            # print(corpus[i],words[j])
            for j, word in enumerate(words):
                print(i,lookup[word],j,word)
                result[i][lookup[word]] +=1
                # print(result)
    return result

print(retryRetry(corpus))


# (0, 0, 0, 'hey')
# (0, 1, 1, 'ho')
# (0, 0, 2, 'hey')
# (1, 0, 0, 'hey')
# (1, 1, 1, 'ho')
# (1, 0, 2, 'hey')
# (1, 0, 3, 'hey')
# (2, 0, 0, 'hey')
# (2, 0, 1, 'hey')
# (2, 0, 2, 'hey')

# {'hey': 0, 'ho': 1}
# [[0, 0], [0, 0], [0, 0]]
# [[1, 0], [1, 0], [1, 0]]
# [[1, 1], [1, 1], [1, 1]]
# [[2, 1], [2, 1], [2, 1]]
# [[3, 1], [3, 1], [3, 1]]
# [[3, 2], [3, 2], [3, 2]]
# [[4, 2], [4, 2], [4, 2]]
# [[5, 2], [5, 2], [5, 2]]
# [[6, 2], [6, 2], [6, 2]]
# [[7, 2], [7, 2], [7, 2]]
# [[8, 2], [8, 2], [8, 2]]
# [[8, 2], [8, 2], [8, 2]]
# [Finished in 0.066s]

# I can't understand why they are all updating...
