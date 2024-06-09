def increasing(arr: list):
    return sorted(arr)


def decreasing(arr: list):
    return sorted(arr, reverse=True)


arr = [10, 20, 30, 40, 50]

print(increasing(arr))
print(decreasing(arr))
