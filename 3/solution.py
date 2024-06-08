def func(arr: list):
    s = sorted(arr)
    second_smallest = s[1]
    second_largest = s[-2]
    return second_largest, second_smallest


print(func([10, 20, 30, 40, 50, 60, 70, 80]))
