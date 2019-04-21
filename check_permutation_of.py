import collections

def check_permutation_of(string1,string2):
    """Worst-case time complexity is O(n)."""
    if len(string1) != len(string2): #O(1)
        return False
    return collections.Counter(string1) == collections.Counter(string2) #O(n+n) to make the dictionaries
                                                                        #O(n+n) to compare equality?
                                                                        #so O(4n) == O(n).

string1 = 'ABC'
string2 = 'CBA'
string3 = "CCBA"
string4 = "ABCC"

print(check_permutation_of(string1,string3))
