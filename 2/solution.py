def largest_number(arr: list):
    return max(arr)


def largest_num(arr: list):
    largest = 0

    for i in arr:
        if i > largest:
            largest = i

    return largest

print(largest_num([1, 2, 3, 4, 5, 0, -5]))
print(largest_number([1, 2, 3, 4, 5, 0, -5]))
