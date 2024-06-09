def max_and_min_digit(num: int):
    arr = [int(x) for x in str(num)]
    arr.sort()
    return arr[0], arr[-1]


print(max_and_min_digit(2547810))
