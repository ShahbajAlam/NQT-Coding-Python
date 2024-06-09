def change_alphabets(a: str):
    result = ""

    for i in a:
        if i == "z":
            result += "a"
        elif i == "Z":
            result += "A"
        else:
            result += chr(ord(i) + 1)

    return result


print(change_alphabets("admszya"))
