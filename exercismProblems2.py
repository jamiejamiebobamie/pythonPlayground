"""
from: https://exercism.io/my/solutions/28b4204dddb44503a7b205283181bbc9

Introduction

Given a phrase, count the occurrences of each word in that phrase.

For example for the input "olly olly in come free"

olly: 2
in: 1
come: 1
free: 1
Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
Running the tests

To run the tests, run the appropriate command below (why they are different):

Python 2.7: py.test word_count_test.py
Python 3.4+: pytest word_count_test.py
Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version): python -m pytest word_count_test.py

Common pytest options
-v : enable verbose output
-x : stop running tests on first failure
--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the $EXERCISM_WORKSPACE/python/word-count directory.

You can find your Exercism workspace by running exercism debug and looking for the line that starts with Workspace.

For more detailed information about running tests, code style and linting, please see Running the Tests.

Source

This is a classic toy problem, but we were reminded of it by seeing it in the Go Tour.

Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise."""

from collections import Counter as count

def wordCount(phrase):
    arrayOfWords = phrase.split(" ")
    histogram = count(arrayOfWords)
    # print(histogram)
    print("\n")
    for key in histogram:
        print(key + ": " + str(histogram[key]))

    print("\n")



phrase = "olly olly in come free"
wordCount(phrase)


"""
from: https://exercism.io/my/solutions/cf310fba4f394d43b2bbb1807e8409fa

Introduction

Correctly determine the fewest number of coins to be given to a customer such that the sum of the coins' value would equal the correct amount of change.

For example

An input of 15 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) or [5, 10]
An input of 40 with [1, 5, 10, 25, 100] should return one nickel (5) and one dime (10) and one quarter (25) or [5, 10, 25]
Edge cases

Does your algorithm work for any given set of coins?
Can you ask for negative change?
Can you ask for a change value smaller than the smallest coin value?
Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")
Running the tests

To run the tests, run the appropriate command below (why they are different):

Python 2.7: py.test change_test.py
Python 3.4+: pytest change_test.py
Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version): python -m pytest change_test.py

Common pytest options
-v : enable verbose output
-x : stop running tests on first failure
--ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the $EXERCISM_WORKSPACE/python/change directory.

You can find your Exercism workspace by running exercism debug and looking for the line that starts with Workspace.

For more detailed information about running tests, code style and linting, please see Running the Tests.

Source

Software Craftsmanship - Coin Change Kata https://web.archive.org/web/20130115115225/http://craftsmanship.sv.cmu.edu:80/exercises/coin-change-kata

Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise."""


# def change(value, arrayOfCoinValues):
#     options = arrayOfCoinValues
#     myCoins = []
#     def __helper(valueLeft, i, chosen):
#         # chosen.append("hi")
#         # return chosen
#         # coinsChosenThusFar = chosen
#         if valueLeft == 0:
#             return chosen
#         elif valueLeft > 0:
#             if i + 1 < len(options):
#                 i+=1
#                 chosen.append(options[i])
#                 return __helper(valueLeft-options[i], i, chosen)
#             else:
#                 i = 1
#                 return __helper(valueLeft-options[i], i, chosen)
#         else:
#             chosen = []
#             i = 1
#             return __helper(valueLeft-options[i], i, chosen)
#
#     return __helper(value, 0, myCoins)

# https://stackoverflow.com/questions/12520263/recursive-change-making-algorithm
def min_change(V, C):
    def min_coins(i, aC):
        print(i, aC)
        if aC == 0:
            return 0
        elif i == -1 or aC < 0:
            return float('inf')
        else:
            return min(min_coins(i-1, aC), 1 + min_coins(i, aC-V[i]))
    return min_coins(len(V)-1, C)

print(min_change([10,20,1], 100))
