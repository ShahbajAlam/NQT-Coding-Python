def change_case(s: str):
    result = ""

    for i in s:
        if i.isupper():
            result += i.lower()
        if i.islower():
            result += i.upper()

    return result


print(change_case("I am Shahbaj Alam"))
