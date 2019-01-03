#https://www.hackerrank.com/challenges/new-year-chaos/problem


# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.
# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if and  bribes , the queue will look like this: .
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
# Function Description
# Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
# minimumBribes has the following parameter(s):
# q: an array of integers
# Input Format
# The first line contains an integer , the number of test cases.
# Each of the next  pairs of lines are as follows:
# - The first line contains an integer , the number of people in the queue
# - The second line has  space-separated integers describing the final state of the queue.
# Constraints
#
#
# Subtasks
# For  score
# For  score
# Output Format
# Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.
# Sample Input
# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# Sample Output
# 3
# Too chaotic

#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q): #O(n**2) time complexity
    minB = 0
    q.reverse() #this adds to time complexity, but you want to handle the back of the line first, by iterating through them first, because you only move forward in line, so person 1 and person 2 are less important
    for i, b in enumerate(q):
        if len(q) - i != b: #if the item is out of place
            # print((b, b - (len(q) - i)))
            if b - (len(q) - i) > 0: #check to see if it's moved upward
                if b - (len(q) - i) < 3: #check to see if it's moved more than two spaces up
                    minB += b - (len(q) - i) #if it hasn't moved more than two, add the number it has moved to the total bribes
                else:
                    return "Too chaotic." #if it has moved more than two, exit the function and arrest the cheaters!
    return minB #return the total bribes.


# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         q = list(map(int, input().rstrip().split()))
#
#         minimumBribes(q)


q = [1,2,3,5,4,6,7,9,8]
p = [9,2,3,4,5,6,7,8]

o = [2,4,3,1,5,6,7,9,8]

print(minimumBribes(o))
