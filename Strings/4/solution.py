def reverse_arr1(arr: list):
    result = []

    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])

    return result


def reverse_arr2(arr: list):
    return list(reversed(arr))


print(reverse_arr1([10, 20, 30, 40, 50]))
print(reverse_arr2([10, 20, 30, 40, 50]))
