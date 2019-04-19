

LOOKUP = {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i","10":"j","11":"k", "12":"l","13":"m","14":"n","15":"o","16":"p", "17":"q","18":"r","19":"s","20":"t","21":"u","22":"v", "23":"w","24":"x","25":"y","26":"z",}


def count_encodings(string_integer):

    count = i = 0

    while i+1 < len(string_integer):
        lookup = string_integer[i]+string_integer[i+1]
        if lookup in LOOKUP:
            count+=2
            i+=2
        else:
            i+=1
    else:
        last_two_digits = string_integer[-2:]
        if string_integer[-1] in LOOKUP and last_two_digits in LOOKUP and string_integer[-1] == string_integer[-2] and len(string_integer) > 2:
            count+=1

    return count

# string_integer = '111'
# string_integer = '1482686'
string_integer = '94325454'
# string_integer = '11'

print(count_encodings(string_integer))
