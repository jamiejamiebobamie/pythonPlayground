"""
Elements of the Programming Interview in Python
pg. 74 "Compute all Mnemonics for a Phone Number"

Write a program which takes as input a phone number, specified as a string of digits,
and returns all possible character sequences that correspond to the phone number.
The cell phone keypad is specified by a mapping that takes a digit and returns
the corresponding set of characters. The character sequences do not have to be legal
words or phrases.

"""


def mnemonics(numberString):
    result = []
    lookup = { "1":"", "2":['A','B','C'], "3":['D','E','F'], "4":['G','H','I'], "5":['J','K','L'], "6":['M','N','O'], "7":['P','Q','R','S'],"8":['T','U','V'],"9":['W','X','Y','Z'],"0": ""}

    for nums in numberString:
        # mini
        for n in lookup[nums]:
            result.append(n)
    return result

print(mnemonics("2222222"))


# in process...
