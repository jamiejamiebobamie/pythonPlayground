A = [1,2,3,4,5,6,7,7]

p = iter(A)
while p:
    print(next(p))



# https://www.programiz.com/python-programming/methods/built-in/next:

# random = [5, 9]
#
# # converting list to iterator
# randomIterator = iter(random)
#
# # Output: 5
# print(next(randomIterator, '-1'))
#
# # Output: 9
# print(next(randomIterator, '-1'))
#
# # randomIterator is exhausted
# # Output: '-1'
# print(next(randomIterator, '-1'))
# print(next(randomIterator, '-1'))
# print(next(randomIterator, '-1'))
#
# # while A:
# #     print(next(A))
