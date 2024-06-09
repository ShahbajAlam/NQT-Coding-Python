def is_harshad_number(num: int):
    sum_of_digits = sum([int(x) for x in str(num)])

    if num % sum_of_digits == 0:
        return True
    return False


for i in range(1, 50):
    if is_harshad_number(i):
        print(i, end=" ")
