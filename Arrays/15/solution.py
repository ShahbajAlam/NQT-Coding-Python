def symmetric_pair(arr: list[tuple]):
    result = []

    for a, b in arr:
        if (b, a) in arr:
            result.append((a, b))

    return result


print(symmetric_pair([(10, 20), (20, 30), (30, 40), (20, 10)]))
