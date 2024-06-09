def remove_duplicates(a: str):
    result = ""

    for i in a:
        if i not in result:
            result += i

    return result


print(remove_duplicates("naheed"))
