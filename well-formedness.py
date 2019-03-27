"""

Write a program to test if a string made up of the characters
'(', ')', '[', ']', '{', and '}' is well-formed.

Elements of Programming Interviews pg. 102

see "balanced.py" in this directory for a similar problem.

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

s = "{{[()]}}"#well-formed
s="{{{{[[[)))}}}}"#not well-formed

def wellFormed(s):
    #stack to add opening characters to
    stack = []
    lookup = {"}":"{", ")":"(", "]":"["}
    for c in s:
    #if c is a closing character
        if c == "}" or  c == ")" or  c == "]":
            #if the stack of opening characters is not empty
            if len(stack):
                if stack.pop() != lookup[c]:#need to compare the popped element with the lookup
                    return False
            #if the stack is empty, a closing character came before an opening one
            else:
                return False
        #c is an opening character, add it to the stack
        else:
            stack.append(c)
    #if we get through the list and the stack isn't empty return false
    if len(stack):
        return False
    else:
        return True

print(wellFormed(s))
