def sum_of_nums1(n: int):
    result = 0

    for i in range(1, n + 1):
        result += i

    return result


def sum_of_nums2(n: int):
    return (n * (n + 1)) / 2


print(sum_of_nums1(10))
print(sum_of_nums2(10))
