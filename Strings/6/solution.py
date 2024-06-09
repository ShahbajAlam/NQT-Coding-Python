def alphabets_only(a: str):
    result = ""

    for i in a:
        if i.isalpha():
            result += i

    return result


print(alphabets_only("a1b2c3d4e"))
