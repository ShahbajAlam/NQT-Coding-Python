def helper(word: str):
    result = ""
    for i in range(len(word)):
        if i == 0 or i == len(word) - 1:
            result += word[i].upper()
        else:
            result += word[i]

    return result


def capitalize(a: str):
    a = a.lower()
    words = a.split()
    result = []

    for word in words:
        result.append(helper(word))

    return " ".join(result)


print(capitalize("i am shahbaj alam"))
