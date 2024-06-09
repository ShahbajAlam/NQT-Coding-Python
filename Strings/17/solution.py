def remove_chars(s1: str, s2: str):
    result = ""

    for i in s1:
        if i not in s2:
            result += i

    return result


print(remove_chars("abcdefg", "acg"))
