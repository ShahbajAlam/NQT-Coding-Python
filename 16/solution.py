def max_product(arr: list):
    result = arr[0]

    for i in range(len(arr)):
        mul = arr[i]

        for j in range(i + 1, len(arr)):
            result = max(result, mul)
            mul = mul * arr[j]

        result = max(result, mul)

    return result


print(max_product([1, -2, -3, 0, 7, -8, -2]))
