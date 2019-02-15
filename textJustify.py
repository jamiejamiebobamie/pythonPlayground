# https://leetcode.com/problems/text-justification/
#
# Given an array of words and a width maxWidth,
# format the text such that each line has exactly
# maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach;
# that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that
# each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# Note:
#
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
# Example 1:
#

#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
# Example 3:
#
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

array = ["This", "is", "an", "example", "of", "text", "justification."]

def justify(array, width):
    size = len(array)
    a = []
    while len(array) > 0:
            arr = []
            count = 0
            while count < width and len(array) != 0:
                if count + len(array[-1]) + len(arr) < width:
                    if len(array) == size:
                        count += len(array[-1])
                        arr.append(" "*(width - count))
                        arr.append(array.pop(-1))
                    else:
                        count += len(array[-1])
                        arr.append(array.pop(-1))
                else:
                    count = (width - count)//len(arr)
                    for word in arr:
                        word += " "*count
                    a.append([list(reversed(arr)), count])
                    break
            else:
                a.append([list(reversed(arr)), width - ((width - count)//len(arr))*count ])
                break
    return a
    # else:
    #     return "sorry one or more of your words is too big for the width."

    #
    # ar = []
    # line = ''
    # i = 0
    # while
    # while len(line) < width:
    #     line += array[i] + " "
    #
    #     i += 1
    # print(line)

print(list(reversed(justify(array, 16))))
