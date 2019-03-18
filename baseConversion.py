"""This is the problem from page 69 of Elements of Programming Interviews in Python

Write a function that takes in a number as a string (example: "314") and two integers (example: 2, 4).
The first number is the base of the string and the second number is the base of what the returned strign needs to be.

NOTE: The book wants the output to be some kind of abbreviated output (for input 615, 7, 13, the output is"1A7").
Not doing that...
"""

def convertBase(inp, baseFrom, baseTo):
    # inp = list(inp).reverse()
    number = 0
    for i, _ in enumerate(inp):
        # print(i)
        number += int(inp[len(inp)-1-i]) * (baseFrom**i)
        # print(number, int(inp[len(inp)-1-i]), i)
    return number


print(convertBase("314", 10, 2))
