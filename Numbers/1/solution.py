def palindrome1(num: int):
    result = ""

    for i in str(num):
        result = i + result

    return str(num) == result


def palindrome2(num: int):
    result = ""

    for i in reversed(str(num)):
        result += i

    return result == str(num)


def palindrome3(num: int):
    s = str(num)
    l = list(s)
    l.reverse()
    l = "".join(l)

    return l == s


print(palindrome1(123))
print(palindrome1(12321))

print(palindrome2(123))
print(palindrome2(12321))

print(palindrome3(123))
print(palindrome3(12321))
