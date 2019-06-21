# problem1


# Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x <= 10n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 <= x <= 100,
#              excluding 11,22,33,44,55,66,77,88,99

# https://leetcode.com/problems/count-numbers-with-unique-digits/

#Bruteforce:
def uniqueDigits(n):
    count = 0
    for _ in range(10**n):
        test = str(_)
        uniqueChars = set()
        unique = True
        for char in test:
            if char in uniqueChars:
                unique = False
                break
            uniqueChars.add(char)
        if unique:
            print(test)
            count+=1

    return count

print(uniqueDigits(3))

# O(n**2) time complexity (sort of)
# O(n) space complexity (sort of)

# I bet there's some trick having to do with the original duplicates that scales with n.
# 99, 102, 103, ..., 109-120,123,

# 9 is the first missing values
# next is 90?
# nope. 739






# problem 2

"""Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address,
mail sent there will be forwarded to the same address without dots in the local name.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
(Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored.
This allows certain emails to be filtered, for example m.y+name@email.com
will be forwarded to my@email.com.
(Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.
How many different addresses actually receive mails?



Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character."""



A = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def howMany(A):
    dict = {}
    for e in A:
        email = ""
        local = True
        plus = False
        for char in e:
            if local:
                if char == '@':
                    email += char
                    local = False
                elif char == "+":
                    plus = True
                elif char == ".":
                    continue
                elif plus == False:
                    email += char
            else:
                email += char
        if email in dict:
            dict[email] += 1
        else:
            dict[email] = 1
    return len(dict)

print(howMany(A))

#Nicolai's solution:
#https://gist.github.com/nsafai/458005c25c477456a58fa3801aba3fe8#file-uniqueemails-py-L14
class Solution:
    def numUniqueEmails(self, emails):
        uniques = set() # A set can not contain duplicates
        for email in emails:
            name, domain = email.split("@")
            if "+" in name:
                name = name.split("+")[0].replace(".", "") # grab everything before "+", remove "."
            else:
                name = name.replace('.', "") # remove "."
            cleanEmail = name + "@" + domain # reassemble emails
            uniques.add(cleanEmail) # add cleanEmail to set, which will not accept duplicates
        return len(uniques) # return length of uniques to get number of uniques
