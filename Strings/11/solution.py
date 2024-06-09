def frequency(a: str):
    d = dict()

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


print(frequency("shahbaj"))
