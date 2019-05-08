"""There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can
climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X."""


def climb_stairs(n):
    """Solving for the base case of climbing 1 or 2 stairs."""

    def __recursive_factorial_helper(n):
        """A recursive factorial helper function that might not be necessary..."""
        print(n)
        if n == 1:
            return n
        return n* __recursive_factorial_helper(n-1)

    remainder = n % 2
    if not remainder:
        return n+1
    else:
        return n+1+remainder*2
        #if 5:
        # 1, 1, 1, 1, 1
        #
        # 2, 1, 1, 1
        # 1, 2, 1, 1
        # 1, 1, 2, 1
        # 1, 1, 1, 2
        #
        # 2, 2, 1
        # 1, 2, 2
        # 2, 1, 2

        #if 3:
        # 1, 1, 1
        #
        # 2, 1
        # 1, 2




def climb_stairs_X(n, *X):
    remainders = [n % x for x in X]
    # print(remainders)
    return remainders


# print(climb_stairs(3))

#if the number of possible steps are 1,2,3

"""1, 1, 1, 1, 1, 1

1, 1, 2, 1, 1
2, 1, 1, 1, 1
1, 1, 1, 1, 2

3,1,2
3,2,1
1,2,3

3,3
3,1,1
1,1,3


2, 2, 1, 1
1, 1, 2, 2

2, 2, 2"""

# print(climb_stairs_X(6,1,2,3,4))

# def stairs(n,*X):
    # def __recursive_counter(numbers,count,n,*X):
    #     if n == 0:
    #         return max(count, len(numbers))
    #     for x in X:
    #         print(numbers,x,n,count)
    #         if n-x >= 0:
    #             numbers.add(x)
    #             count+=__recursive_counter(numbers,count,n-x,*X)
    #         else:
    #             # numbers = []
    #             break
    #     return max(count, len(numbers))
    #
    # return __recursive_counter(set(),0,n,*X)

def stairs(n,*X):
    def __recursive_counter(n,*X):
        for x in X:
            if n == x:
                return x
            return __recursive_counter(n-1,x)
    result = 0

    for x in X:
        result += __recursive_counter(n,x)
    return result


# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

print(stairs(4,1,2))
