"""

My attempt at making a bi-directional map / multi-map, also known as a hashbag.

TO-DO: Lookup the syntax of 'super(hashBag, self).__delitem__(self[key])''

"""


class hashBag(dict):
    def __init__(self):
        pass


    def __setitem__(self, key, value):
        if key in self: #remove both the key-value and the value-key if present:
            super(hashBag, self).__delitem__(self[key])
            super(hashBag, self).__delitem__(key)
        super(hashBag, self).__setitem__(key, value) #update the key with the new value
        super(hashBag, self).__setitem__(value, key)


P = hashBag()

print(P)

P['i'] = 1
print(P)

P['i'] = 2
print(P)
print(P.get(2))
