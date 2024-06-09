def sort_acc_to_another_arr(arr1: list, arr2: list):
    present = [x for x in arr1 if x in arr2]
    missing = [x for x in arr1 if x not in arr2]
    missing.sort()

    result = []
    for i in arr2:
        c = present.count(i)
        result.extend([i] * c)
    result.extend(missing)

    return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(sort_acc_to_another_arr(arr1, arr2))
