def find_repeating(arr: list):
    result = []

    for i in arr:
        if arr.count(i) > 1 and i not in result:
            result.append(i)

    return result


print(find_repeating([10, 20, 30, 30, 40, 40, 40, 10, 50]))
