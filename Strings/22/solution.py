def check_subset(arr1: list, arr2: list):
    is_subset = True
    for i in arr2:
        if i not in arr1:
            is_subset = False
            break

    return is_subset


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1, 2]
print(check_subset(arr1, arr2))
