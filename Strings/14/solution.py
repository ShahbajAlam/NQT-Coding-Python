from collections import Counter


def max_occuring(a: str):
    c = Counter(a)
    c = c.most_common()[0][0]

    return c


print(max_occuring("abcbbb"))
