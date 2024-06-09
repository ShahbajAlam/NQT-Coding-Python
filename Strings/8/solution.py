def remove_brackets(a: str):
    result = ""

    for i in a:
        if i not in "({[]})":
            result += i

    return result


print(remove_brackets("(a+b)[a-b]"))
