"""

Given a stirng of text and a number 'k', find 'k' words in the given text that appear
most frequently.

Return an array of words in decreasing order.

"""

import heapq
from collections import Counter as count

def mostFrequent(text, k):
    histogramOfFreq = {}

    word = ""
    for char in text:
        if char == " ":
            if word in histogramOfFreq:
                histogramOfFreq[word] += 1
            else:
                histogramOfFreq[word] = 1
            word = ""
        else:
            word += char

    print(histogramOfFreq.keys())





    A = text.split()
    hist = count(A)

    keys = hist.keys()
    values = hist.values()

    print(hist)
    print(keys)
    print(values)

    myHeap = heapq.heapify(A)
    return heapq.nlargest(k, values)



text = "hello, baby bay bay baby yeah yeah yeah no no no yes"

k = 2

print(mostFrequent(text, k))
