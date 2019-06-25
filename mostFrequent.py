"""

Given a stirng of text and a number 'k', find 'k' words in the given text that appear
most frequently.

Return an array of words in decreasing order.

"""


# breakout problem w/o editing:

# import heapq
# from collections import Counter as count
#
# def mostFrequent(text, k):
#     histogramOfFreq = {}
#
#     word = ""
#     for char in text:
#         if char == " ":
#             if word in histogramOfFreq:
#                 histogramOfFreq[word] += 1
#             else:
#                 histogramOfFreq[word] = 1
#             word = ""
#         else:
#             word += char
#
#     print(histogramOfFreq.keys())
#
#
#
#
#
#     A = text.split()
#     hist = count(A)
#
#     keys = hist.keys()
#     values = hist.values()
#
#     print(hist)
#     print(keys)
#     print(values)
#
#     myHeap = heapq.heapify(A)
#     return heapq.nlargest(k, values)
#
#
#
# text = "hello, baby bay bay baby yeah yeah yeah no no no yes"
#
# k = 2
#
# print(mostFrequent(text, k))


# breakout problem w/ editing:
import heapq
from collections import Counter as count

def mostFrequent(text, k):
    wordsArray = text.split(" ") #O(n)
    histogramOfWords = count(wordsArray) #O(n)

    print(histogramOfWords)

    lenHistogramOfWords = len(histogramOfWords)
    results = []

    while len(results) < k and lenHistogramOfWords > 0:
        word = None
        currentMax = float('-inf')

        for key in histogramOfWords:
            tempMax = currentMax
            currentMax = max(currentMax, histogramOfWords[key])
            if currentMax != tempMax or word == None:
                word = key

        results.append(word)
        del histogramOfWords[word]
        lenHistogramOfWords -= 1

    return results

text = "hello, baby bay bay baby yeah yeah yeah no no no yes"

k = 1

print(mostFrequent(text, k))
