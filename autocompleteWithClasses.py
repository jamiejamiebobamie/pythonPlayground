'''An autocomplete function. Call the function in the terminal and
    type a prefix to see all possibile words that can be made with that prefix.

TO-DO: Rewrite code in Javascript and then make a website
       that hosts the already built Trie in a database and pulls from it
       dynamically, displaying the possibile words in a drop-down menu as the user types.'''

import sys

class Trie:
    """A Trie specificially made to hold a dictionary of words."""

    def __init__(self):
        self.array = self.dict() #Array of dictionary words
        self.root = self.buildTrie(self.array)

    class TrieNode:
        def __init__(self, value=None, i=None):
            self.value = value
            self.dict = {}
            self.end = False
            self.count = 0 # how many words contain this prefix
            self.depth = i # how many letters into the word, 0 = first letter

    def buildTrie(self, array):
        root = self.TrieNode()
        current = root
        for word in array:
            for i, char in enumerate(word):
                c = char.lower()
                if c not in current.dict:
                    current.dict[c] = self.TrieNode(c,i)
                current.count += 1
                current = current.dict[c]
            current.end = True
            current = root
        return root

    def dict(self):
        """opens the dictionary-words file at the path and assigns the file to 'f'
        reads 'f' and splits each word into an array element of the 'words' array
        closes the file 'f'
        and returns the array of dictionary words
        """
        f = open("/usr/share/dict/words", "r")
        words = f.read().split()
        f.close()
        return words

    def findWords(self, pre):
        def __findWordsHelper(node, w, sC): #current node, string built so far, the count of all possible suffixes
            co = sC #passing off the suffix count to the interior scope
            for key in node.dict:
                c = w #passing off the built word to the interior scope
                c += node.dict[key].value
                if node.dict[key].end == True:
                    words.append(c)
                    if co < 0: # if the suffix you enter is a complete word (like 'ant')...
                        return c # don't stop until all of the suffixes have been exhausted
                    else:
                        co -= 1
                __findWordsHelper(node.dict[key], c, co)

        word = pre
        words = []
        current = self.root

#move up to the correct point in the dictionary
        for char in pre:
            if char in current.dict:
                current = current.dict[char]

#the correct node in the trie based on the prefix
        known = current
        suffixCount = known.count

# Note to self functions within class methods don't need 'self.'
        __findWordsHelper(known, pre, suffixCount)
        return words

if __name__ == "__main__":
    prefix = str(sys.argv[1]).lower() #Note: uppercase letters would otherwise affect output
    new = Trie()
    print(new.findWords(prefix)) #type in prefix
