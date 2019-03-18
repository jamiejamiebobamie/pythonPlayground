"""This is the problem from page 69 of Elements of Programming Interviews in Python

Write a function that takes in a number as a string (example: "314") and two integers (example: 2, 4).
The first number is the base of the string and the second number is the base of what the returned strign needs to be.

NOTE: The book wants the output to be some kind of abbreviated output (for input '615', 7, 13, the output is"1A7").
Not doing that...
"""

def convertBase(inp, baseFrom, baseTo):
    def _turn_into_decimal():
        number = 0
        for i, _ in enumerate(inp):
            number += int(inp[len(inp)-1-i]) * (baseFrom**i)
        return str(number)

    def _turn_into_baseTo(num):
        number = 0
        for i, _ in enumerate(num):
            number += int(inp[len(inp)-1-i]) * (baseTo**i)
        return number

    return _turn_into_baseTo(_turn_into_decimal())

print(convertBase('111', 10, 2))
