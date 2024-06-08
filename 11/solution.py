def remove_duplicates(arr: list):
    return sorted(list(set(arr)))


print(remove_duplicates([10, 10, 10, 20, 30, 30, 40, 50, 50]))
