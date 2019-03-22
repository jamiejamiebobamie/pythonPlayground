

"""

Implement encode and decode functions for string compression.

Example:
    encoder:
        Input: "aaaabcccaa"
        Output: "4a1b3c2a"
    decoder:
        Input: "3e4f2e"
        Output: "eeeffffee"
"""


def encoder(s):

    result = ""
    current = s[0]
    count = 0

    for i, c in enumerate(s):
        #handles the characters of the string up until the last repeated character
        if c == current:
            count+=1
        else:
            result += str(count) + current
            count = 1
            current = c
        #add the last repeated letter to the result
        if i == len(s)-1:
            result += str(count) + current
    return result

print(encoder('heyyyyyyy'))


def decoder(s):
    result = ""
    for i, c in enumerate(s):
        if i%2 == 0:
            result += int(s[i])*s[i+1]
    return result

print(decoder("1h1e7y"))
