corpus = [["hey ho hey"], ["hey ho hey hey"], ["hey hey hey"]]


def bow(corpus):

    lookup = {}

    indexCount = 0


    for array in corpus:
        for line in array:
            string = line.split(" ")
            for word in string:
                if word not in lookup:
                    lookup[word] = indexCount
                    indexCount+=1
    result = [[0]* len(lookup)] * len(corpus)

    print(lookup)
    print(result)

    for i, array in enumerate(corpus):
        # print(i)
        for line in array:
            string = line.split(" ")
            for word in string:
                result[i][lookup[word]]+=1
                print(word, i, lookup[word], result)
            # print(result)

    return result

print(bow(corpus))
