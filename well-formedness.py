"""

Write a program to test if a string made up of the characters
'(', ')', '[', ']', '{', and '}' is well-formed.

"""



# def wellFormed(s):
#     opening = {'{':list(),'[':list(),'(':list()}
#     closing = {'{':'}','[':']','(':')'}
#
#     for c in s:
#         if c in opening:
#             opening[c].append(closing[c])
#     return opening
#         # else:
#         #     opening[closing[c]]
#
# print(wellFormed(s))

s = "{{[()]}}"
s="{{{}}}"

def wellFormed(s):
    stack = []
    for c in s:
        if c == "}" or  c == ")" or  c == "]":
            if len(stack):
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if len(stack):
        return False
    else:
        return True

print(wellFormed(s))
