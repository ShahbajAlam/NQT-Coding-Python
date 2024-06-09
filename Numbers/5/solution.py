def is_armstrong(num: int):
    result = 0

    for i in str(num):
        result += int(i) ** 3

    return num == result


print(is_armstrong(153))
print(is_armstrong(120))
print(is_armstrong(407))
