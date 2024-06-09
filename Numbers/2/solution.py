def is_palindrome(num: int):
    result = ""

    for i in reversed(str(num)):
        result += i

    return result == str(num)


def show_palindrome(x, y):
    for i in range(x, y + 1):
        if is_palindrome(i):
            print(i)


show_palindrome(200, 300)
