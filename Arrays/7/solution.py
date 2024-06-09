def sum_of_elements(arr: list[int]):
    return sum(arr)


def sum_of_elems(arr: list[int]):
    total = 0

    for i in arr:
        total += i

    return total


arr = [10, 20, 30, 40, 50]

print(sum_of_elems(arr))
print(sum_of_elements(arr))
