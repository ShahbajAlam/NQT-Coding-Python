def mean(arr: list[int]):
    return sum(arr) / len(arr)


def median(arr: list[int]):
    s = sorted(arr)
    size = len(s)
   
    if size % 2 != 0:
        return s[size // 2]
    else:
        return (s[size // 2] + s[(size // 2) - 1]) / 2


print(mean([1, 3, 4, 2, 6, 5, 8, 7]))
print(median([1, 3, 4, 2, 6, 5, 8, 7]))
