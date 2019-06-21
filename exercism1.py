#https://exercism.io/my/solutions/cf2a771d09704ce5802743f462a36912
#Exercism problem 1
"""
Generate the lyrics of the song 'I Know an Old Lady Who Swallowed a Fly'.

While you could copy/paste the lyrics, or read them from a file,
this problem is much more interesting if you approach it algorithmically.

This is a cumulative song of unknown origin.

This is one of many common variants.

I know an old lady who swallowed a fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a spider.
It wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a bird.
How absurd to swallow a bird!
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cat.
Imagine that, to swallow a cat!
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a dog.
What a hog, to swallow a dog!
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a goat.
Just opened her throat and swallowed a goat!
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cow.
I don't know how she swallowed a cow!
She swallowed the cow to catch the goat.
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a horse.
She's dead, of course!





Exception messages

Sometimes it is necessary to raise an exception.
When you do this, you should include a meaningful error message to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
Not every exercise will require you to raise an exception,
but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type.
For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
Running the tests

To run the tests, run the appropriate command below (why they are different):

Python 2.7: py.test food_chain_test.py
Python 3.4+: pytest food_chain_test.py
Alternatively, you can tell Python to run the pytest module
(allowing the same command to be used regardless of Python version): python -m pytest food_chain_test.py

Common pytest options
-v : enable verbose output
-x : stop running tests on first failure
--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

Submitting Exercises

Note that, when trying to submit an exercise,
make sure the solution is in the $EXERCISM_WORKSPACE/python/food-chain directory.

You can find your Exercism workspace by running exercism debug
and looking for the line that starts with Workspace.

For more detailed information about running tests,
code style and linting, please see Running the Tests."""



text = """I know an old lady who swallowed a fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a spider.
It wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a bird.
How absurd to swallow a bird!
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cat.
Imagine that, to swallow a cat!
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a dog.
What a hog, to swallow a dog!
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a goat.
Just opened her throat and swallowed a goat!
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a cow.
I don't know how she swallowed a cow!
She swallowed the cow to catch the goat.
She swallowed the goat to catch the dog.
She swallowed the dog to catch the cat.
She swallowed the cat to catch the bird.
She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
She swallowed the spider to catch the fly.
I don't know why she swallowed the fly. Perhaps she'll die.

I know an old lady who swallowed a horse.
She's dead, of course!
"""

from collections import Counter as count

array = []
entry = []

for word in text:
    if word == " ":
        array.append("".join(entry))
        entry = []
    else:
        entry.append(word)

# print(array)
dict = {}

for i, item in enumerate(array):
    if i > 0:
        dict[array[i-1]] = item


m = 0
l = 1
song = current_word = array[0]

while m < len(array):
    if current_word in dict:
        current_word = dict[current_word]
    else:
        current_word = array[l]
        l+=1
    song = song + " " + current_word
    m+=1
# print(song)


# https://exercism.io/my/solutions/06695796702f4870b3153821989ec329
#Exercism problem 2


"""Introduction

Implement a simple shift cipher like Caesar and a more secure substitution cipher.

Step 1

"If he had anything confidential to say, he wrote it in cipher,
that is, by so changing the order of the letters of the alphabet, that not a word could be made out.
If anyone wishes to decipher these, and get at their meaning,
he must substitute the fourth letter of the alphabet,
namely D, for A, and so with the others."

Ciphers are very straight-forward algorithms
that allow us to render text less readable while still allowing easy deciphering.
They are vulnerable to many forms of cryptoanalysis,
but we are lucky that generally our little sisters are not cryptoanalysts.

The Caesar Cipher was used for some messages from Julius Caesar that were sent afield.
Now Caesar knew that the cipher wasn't very good,
but he had one ally in that respect: almost nobody could read well.
So even being a couple letters off was sufficient so that people couldn't
recognize the few words that they did know.

Your task is to create a simple shift cipher like the Caesar Cipher.
This image is a great example of the Caesar Cipher:

Caesar Cipher

For example:

Giving "iamapandabear" as input to the encode function returns the cipher
"ldpdsdqgdehdu". Obscure enough to keep our message secret in transit.

When "ldpdsdqgdehdu" is put into the decode function it would return the original
"iamapandabear" letting your friend read your original message.

Step 2

Shift ciphers are no fun though when your kid sister figures it out.
Try amending the code to allow us to specify a key and use that for the shift distance.
This is called a substitution cipher.

Here's an example:

Given the key "aaaaaaaaaaaaaaaaaa", encoding the string "iamapandabear" would return the original "iamapandabear".

Given the key "ddddddddddddddddd", encoding our string "iamapandabear" would return the obscured "ldpdsdqgdehdu"

In the example above, we've set a = 0 for the key value. So when the plaintext is added to the key,
we end up with the same message coming out.
So "aaaa" is not an ideal key.
But if we set the key to "dddd", we would get the same thing as the Caesar Cipher.

Step 3

The weakest link in any cipher is the human being. Let's make your substitution
cipher a little more fault tolerant by providing a source of randomness and ensuring
that the key contains only lowercase letters.

If someone doesn't submit a key at all, generate a truly random key of at least 100 characters in length.

Extensions

Shift ciphers work by making the text slightly odd, but are vulnerable to frequency analysis.
Substitution ciphers help that, but are still very vulnerable when the key is
short or if spaces are preserved. Later on you'll see one solution to this problem in the exercise "crypto-square".

If you want to go farther in this field, the questions begin to be about how we can exchange
keys in a secure way. Take a look at Diffie-Hellman on Wikipedia for one of the first implementations of this scheme.

Should I use random or secrets?

Python, as of version 3.6, includes two different random modules.

The module called random is pseudo-random, meaning it does not generate true randomness,
but follows an algorithm that simulates randomness. Since random numbers are generated through a known algorithm,
they are not truly random.

The random module is not correctly suited for cryptography and should not be used,
precisely because it is pseudo-random.

For this reason, in version 3.6, Python introduced the secrets module,
which generates cryptographically strong random numbers that provide the greater security required for cryptography.

Since this is only an exercise, random is fine to use,
but note that it would be very insecure if actually used for cryptography.

Exception messages

Sometimes it is necessary to raise an exception. When you do this,
you should include a meaningful error message to indicate what the source of the error is.
This makes your code more readable and helps significantly with debugging.
Not every exercise will require you to raise an exception, but for those that do,
the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type.
For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
Running the tests

To run the tests, run the appropriate command below (why they are different):

Python 2.7: py.test simple_cipher_test.py
Python 3.4+: pytest simple_cipher_test.py
Alternatively, you can tell Python to run the pytest module (allowing the same
command to be used regardless of Python version): python -m pytest simple_cipher_test.py

Common pytest options
-v : enable verbose output
-x : stop running tests on first failure
--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the
$EXERCISM_WORKSPACE/python/simple-cipher directory.

You can find your Exercism workspace by running exercism debug and looking for
the line that starts with Workspace.

For more detailed information about running tests, code style and linting, please see Running the Tests.

Source

Substitution Cipher at Wikipedia http://en.wikipedia.org/wiki/Substitution_cipher

Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise."""


#step 1

from hashbag import hashBag

def shiftCypher(message):
    LOOKUP = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
                14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    HB = hashBag(LOOKUP)
    built_in_shift = 3
    new_message = ""
    test_message = ""
    # print(message)
    for letter in message:
        if 26 > HB[letter] + built_in_shift:
            lookup = HB[letter] + built_in_shift
        else:
            lookup = HB[letter] + built_in_shift - 26

        new_message += HB[lookup]

    for letter in new_message:
        if 0 < HB[letter] - built_in_shift:
            lookup = HB[letter] - built_in_shift
        else:
            # print(30 - HB[letter] - built_in_shift)
            lookup = 30 - HB[letter] - built_in_shift
        test_message += HB[lookup]

    return new_message, test_message

message = "hellobabyzetagretayabbadabbadoo"
print(shiftCypher(message))


#step 2

def shiftMessageK(message, k):
        LOOKUP = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m',
                    13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
        HB = hashBag(LOOKUP)
        built_in_shift = k
        new_message = ""
        test_message = ""
        # print(message)
        for letter in message:
            if 26 > HB[letter] + built_in_shift:
                lookup = HB[letter] + built_in_shift
            else:
                lookup = HB[letter] + built_in_shift - 26

            new_message += HB[lookup]

        for letter in new_message:
            if -1 < HB[letter] - built_in_shift:
                lookup = HB[letter] - built_in_shift
            else:
                # print(26 - HB[letter] - built_in_shift)
                lookup = 26 - HB[letter] - built_in_shift
            test_message += HB[lookup]

        return new_message, test_message

message = "hellobabyzetagretayabbadabbadoo"
print(shiftMessageK(message,2))


# step 3

import random

def shiftMessageRandomK(message, k=None):

    if k == None:
        keys = []
        for _ in range(len(message)):
            keys.append(random.randint(0,10))

    print(keys)

    LOOKUP = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m',
                13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}
    HB = hashBag(LOOKUP)
    built_in_shift = k
    new_message = ""
    test_message = ""
    for i, letter in enumerate(message):
        if 25 > HB[letter] + keys[i]:
            lookup = HB[letter] + keys[i]
        else:
            lookup = HB[letter] + keys[i] - 25

        new_message += HB[lookup]

    for i, letter in enumerate(new_message):
        if -1 < HB[letter] - keys[i]:
            lookup = HB[letter] - keys[i]
        else:
            # print(26 - HB[letter] - built_in_shift)
            lookup = 26 - HB[letter] - keys[i]
        test_message += HB[lookup]

    return new_message, test_message

message = "hellobabyzetagretayabbadabbadoo"
print(shiftMessageRandomK(message))
#solved the problem, but I seem to be having issues with my edge cases like y and z.
