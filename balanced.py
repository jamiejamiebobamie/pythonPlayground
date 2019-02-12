# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

# string = "(j)(d(ffd)s)a)a)s)"
string = "))"
# string = "(((())))"
# string = "((((("

def balanced(s):
    a = []
    l = len(s)

    for i, c in enumerate(s):
        if c == '(':
            a.append(c)
        if c == ')':
            if len(a) != 0 and i < l:
                a.pop()
            else:
                return False

        print(a)

    return len(a) == 0

print(balanced(string))
