from collections import Counter


def helper(word: str):
    c = Counter(word)
    c = c.most_common()[0][1]
    return c


def highest_repeated_letters(sentence: str):
    words = sentence.split()
    result = Counter()

    for word in words:
        count = helper(word)
        result[word] = count

    return result.most_common()[0][0]


print(highest_repeated_letters("my name is naheed"))
