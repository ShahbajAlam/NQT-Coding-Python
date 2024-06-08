def sort_by_frequency(arr: list):
    return sorted(sorted(arr, reverse=True), key=arr.count)


arr = [2, 5, 2, 8, 5, 6, 8, 8]

print(sort_by_frequency(arr))
