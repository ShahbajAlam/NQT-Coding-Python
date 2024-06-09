def is_palindrome(a: str):
    r = ""
    for i in reversed(a):
        r += i

    return r == a


print(is_palindrome("radar"))
print(is_palindrome("abc"))
