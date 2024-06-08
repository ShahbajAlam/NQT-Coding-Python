from collections import Counter


def frequency1(arr: list):
    return dict(Counter(arr))


def frequency2(arr: list):
    result = dict()

    for i in arr:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1

    return result


print(frequency1([1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6]))
print(frequency2([1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6]))
