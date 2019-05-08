import sys

def dict():
    """Opens the dictionary-words file at the path. Assigns the file to 'f'.
    Reads 'f' and splits each word into a 'words' array element.
    Closes 'f'. Returns the array of dictionary words."""

    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words

# an array of jumbled, unsorted strings to search for
myItems = ["tefon", "sokik", "niumem", "siconu"]

#an array of sorted, jumbled words
myItems_sorted = []
for item in myItems:
    myItems_sorted.append(''.join(sorted(item)))

#a dictionary to hold the words that match the items in myItems_sorted, when the words are sorted.
dictionary_myItems_sorted = {}
for sortedItem in myItems_sorted:
    dictionary_myItems_sorted[sortedItem] = []

#generate an array of words from the dictiobary in an array format
words = dict()

#iterate through the array of dictionary words and check to see if the words
#are five or six characters long.
for word in words:
    if len(word) == 5 or len(word) == 6:
        test_key = ''.join(sorted(word.lower()))
#if the words are 5 or 6 characters long check to see if their sorted version is a key
#in the dictionary_myItems_sorted dictonary. if it is a key, add the word as a value.
        if test_key in dictionary_myItems_sorted:
            dictionary_myItems_sorted[test_key].append(word)

print(dictionary_myItems_sorted)
