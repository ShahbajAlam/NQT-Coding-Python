def replace(num: int):
    result = ""

    for i in str(num):
        if int(i) == 0:
            result += "1"
        else:
            result += i

    return int(result)


print(replace(250140))
