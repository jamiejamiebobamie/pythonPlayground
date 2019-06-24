def isValid(IP_address):
    """A function to test if an IP address is valid.
    An IP address is valid if it contains
    only numbers between 0 and 255 (inclusive) separated by 3 periods.
    Non-numeric characters, leading zeroes ('01'), and repeating zeroes ('000')
    are not allowed."""

    test = "" #test string
    count = 0 #count the periods

    for number in IP_address:
        if number != ".":
            if number.isdigit():
                test += number
            else:
                return IP_address, False
        else:
            test_leading_zeroes = len(test)
            test = int(test)
            if test > 255 or test < 0 or test_leading_zeroes != len(str(test)):
                return IP_address, False
            count += 1
            test = ""

    #test last test string:
    test_leading_zeroes = len(test)
    test = int(test)
    if test > 255 or test < 0 or test_leading_zeroes != len(str(test)):
        return IP_address, False

    return IP_address, count < 4

IP_address = '1.221.255.030'
print(isValid(IP_address))

IP_address = '12.2.3.45'
print(isValid(IP_address))

IP_address = '1.22.33.450'
print(isValid(IP_address))

IP_address = '1.2.3.255'
print(isValid(IP_address))

IP_address = '01.12.3.45'
print(isValid(IP_address))

IP_address = '0.12.3.45'
print(isValid(IP_address))

IP_address = '01.12.3.45.255'
print(isValid(IP_address))

IP_address = '1.12.cool.45.255'
print(isValid(IP_address))

IP_address = '000.12.1.45.255'
print(isValid(IP_address))
