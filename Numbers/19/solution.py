def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def is_strong_num(num: int):
    l = [fact(int(x)) for x in str(num)]
    return num == sum(l)


print("Strong numbers are : ")

for i in range(100000):
    if is_strong_num(i):
        print(i, end=" ")
