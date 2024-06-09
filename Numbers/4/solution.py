def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def show_prime(x, y):
    for i in range(x, y + 1):
        if is_prime(i):
            print(i)


show_prime(100, 200)
