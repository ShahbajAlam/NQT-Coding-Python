def reverse_digits(num: int):
    s = str(num)
    result = ""
    for i in s:
        result = i + result
    return result


print(reverse_digits(1542))
