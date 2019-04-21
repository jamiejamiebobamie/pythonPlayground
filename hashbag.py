"""

My attempt at making a bi-directional map / multi-map, also known as a hashbag.

When a key-value pair is added to the dictionary, an inverse value-key is also inserted.
So you can reference keys by calling the dictionary with the values.

dict[key] = value, dict[value] = key

Initializing the hashBag:
HB = hashBag({2:3, 4:5})
(Must wrap the arguments in curly braces.)

REFERENCE:
https://stackoverflow.com/questions/3318625/how-to-implement-an-efficient-bidirectional-hash-table
https://stackoverflow.com/questions/2390827/how-to-properly-subclass-dict-and-override-getitem-setitem
https://www.pythonforbeginners.com/super/working-python-super-function

"""


class hashBag(dict):
    def __init__(self, *args, **kwargs):
        super(hashBag, self).__init__(*args, **kwargs)
        for key, value in self.items():
            super(hashBag, self).__setitem__(value, key)

    def __setitem__(self, key, value):
        if key in self: #remove both the key-key:value-value and the key-value:value-key if present
            super(hashBag, self).__delitem__(self[key])
            super(hashBag, self).__delitem__(key)
        super(hashBag, self).__setitem__(key, value) #update the key-key with the new value-value
        super(hashBag, self).__setitem__(value, key) #update the key-value with the new value-key
