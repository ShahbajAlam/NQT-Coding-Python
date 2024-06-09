def remove_space(a: str):
    result = ""

    for i in a:
        if i != " ":
            result += i

    return result


print(remove_space("i am shahbaj alam"))
