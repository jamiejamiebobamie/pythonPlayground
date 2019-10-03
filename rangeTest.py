def oddNumbers(l, r):
    if isinstance(l, int) and isinstance(r, int):
        for num in range(l,r+1):
            if num%2:
                print(num)


oddNumbers(1,9)
