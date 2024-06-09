def is_abundant_number(num: int):
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    return sum_of_divisors > num


for i in range(1, 100):
    if is_abundant_number(i):
        print(i, end=" ")
