def sum_of_nums(a: str):
    total = 0

    for i in a:
        if i.isdigit():
            total += int(i)

    return total


print(sum_of_nums("ab12cd34"))
